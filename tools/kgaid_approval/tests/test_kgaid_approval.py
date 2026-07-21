from __future__ import annotations

from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, quote, urlsplit

import pytest

from kgaid_approval import ApprovalError, DocumentationRepository
from kgaid_approval.app import create_app
from kgaid_approval.cli import build_parser
from kgaid_approval.diagnostics import Diagnostics
from kgaid_approval.repository import parse_front_matter
from kgaid_approval.routes import PATH_PARAMETER
from kgaid_approval.web import render_markdown, resolve_document_href


class NavigationParser(HTMLParser):
    """Collect application links, form actions, and hidden form fields from a page."""

    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.form_actions: list[str] = []
        self.hidden_values: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"])
        if tag == "form" and attributes.get("action"):
            self.form_actions.append(attributes["action"])
        if tag == "input" and attributes.get("type") == "hidden" and attributes.get("value"):
            self.hidden_values.append(attributes["value"])


def navigation(response_text: str) -> NavigationParser:
    parser = NavigationParser()
    parser.feed(response_text)
    return parser


def make_app(tmp_path: Path, document_count: int = 3):
    for index in range(1, document_count + 1):
        write_document(
            tmp_path,
            f"nested/document-{index}.md",
            "---\n"
            f"document_id: DOC-{index}\n"
            f"title: Dokument {index}\n"
            "approval_status: pending\n"
            "---\n"
            f"# Dokument {index}\n",
        )
    return create_app(DocumentationRepository(tmp_path), "Krzysztof Olejnik")


def write_document(root: Path, relative_path: str, content: str) -> Path:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def pending_document(title: str, body: str) -> str:
    return f"---\ntitle: {title}\napproval_status: pending\n---\n# {title}\n\n{body}\n"


def draft_document(title: str, body: str) -> str:
    return f"---\ntitle: {title}\napproval_status: draft\n---\n# {title}\n\n{body}\n"


@pytest.mark.parametrize(
    ("current_document", "href", "expected"),
    [
        ("area/source.md", "target.md", "preview:area/target.md"),
        ("area/source.md", "subdir/target.md", "preview:area/subdir/target.md"),
        ("area/deep/source.md", "../target.md", "preview:area/target.md"),
        ("area/source.md", "docs/other/target.md", "preview:other/target.md"),
        (
            "area/source.md",
            "target.md#section-name",
            "preview:area/target.md#section-name",
        ),
        ("area/source.md", "#section-name", "#section-name"),
        ("area/source.md", "target%20name.md", "preview:area/target name.md"),
        ("area/source.md", "extensionless", "extensionless"),
        ("area/source.md", "https://example.com/docs/a.md", "https://example.com/docs/a.md"),
        ("area/source.md", "http://example.com/a.md", "http://example.com/a.md"),
        ("area/source.md", "mailto:docs@example.com", "mailto:docs@example.com"),
        ("area/source.md", "image.png", "image.png"),
        ("area/source.md", "/absolute.md", "/absolute.md"),
        ("area/source.md", "../../outside.md", "../../outside.md"),
        ("area/source.md", "%2e%2e/%2e%2e/outside.md", "%2e%2e/%2e%2e/outside.md"),
        ("area/source.md", "%252e%252e/%252e%252e/outside.md", "%252e%252e/%252e%252e/outside.md"),
    ],
)
def test_resolves_only_safe_local_markdown_links(
    tmp_path: Path, current_document: str, href: str, expected: str
) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()

    resolved = resolve_document_href(
        Path(current_document), href, docs, lambda path: f"preview:{path}"
    )

    assert resolved == expected


def test_directory_link_resolves_to_its_readme(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    write_document(docs, "area/README.md", pending_document("Area", "Area body"))

    resolved = resolve_document_href(
        Path("source.md"), "area/", docs, lambda path: f"preview:{path}"
    )

    assert resolved == "preview:area/README.md"


def test_directory_link_without_readme_is_not_rewritten(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    (docs / "empty").mkdir(parents=True)

    resolved = resolve_document_href(
        Path("source.md"), "empty/", docs, lambda path: f"preview:{path}"
    )

    assert resolved == "empty/"


def test_version_option_prints_runtime_diagnostics(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        build_parser().parse_args(["--version"])

    output = capsys.readouterr().out
    assert exit_info.value.code == 0
    assert "Version:" in output
    assert "Module path:" in output
    assert "Python executable:" in output
    assert "Package location:" in output


def test_home_page_contains_correct_diagnostics(tmp_path: Path) -> None:
    app = make_app(tmp_path, document_count=0)
    diagnostics = app.config["KGAID_DIAGNOSTICS"]

    assert isinstance(diagnostics, Diagnostics)
    assert diagnostics.version
    assert diagnostics.python_executable.is_absolute()
    assert diagnostics.package_location.is_dir()
    assert diagnostics.docs_root == tmp_path.resolve()
    assert diagnostics.approver == "Krzysztof Olejnik"
    assert diagnostics.working_directory.is_absolute()

    response = app.test_client().get("/")
    for label in (
        "Version",
        "Python executable",
        "Package location",
        "Docs root",
        "Approver",
        "Working directory",
    ):
        assert label in response.text
    assert str(tmp_path.resolve()) in response.text
    assert "Krzysztof Olejnik" in response.text


def test_local_document_links_render_through_preview_route_and_are_navigable(
    tmp_path: Path,
) -> None:
    write_document(
        tmp_path,
        "10-knowledge-architecture/11-overview.md",
        pending_document(
            "Overview",
            "See [Artifact Model](12-artifact-model.md) and "
            "[relationship](12-artifact-model.md#relationship-semantics).",
        ),
    )
    write_document(
        tmp_path,
        "10-knowledge-architecture/12-artifact-model.md",
        pending_document("Artifact Model", "## Relationship semantics\n\nExpected target body."),
    )
    client = create_app(DocumentationRepository(tmp_path), "Reviewer").test_client()

    source_response = client.get("/document?path=10-knowledge-architecture/11-overview.md")
    links = navigation(source_response.text).links
    document_links = links[1:]

    assert source_response.status_code == 200
    assert document_links == [
        "/document?path=10-knowledge-architecture/12-artifact-model.md",
        "/document?path=10-knowledge-architecture/12-artifact-model.md#relationship-semantics",
    ]
    target_response = client.get(document_links[0])
    assert target_response.status_code == 200
    assert "Artifact Model" in target_response.text
    assert "Expected target body." in target_response.text


def test_nested_parent_subdirectory_and_encoded_document_links(tmp_path: Path) -> None:
    write_document(
        tmp_path,
        "area/deep/source.md",
        pending_document(
            "Source",
            "[Parent](../parent.md) [Child](subdir/child.md) [Encoded](subdir/document%20żółć.md)",
        ),
    )
    for relative_path, title in [
        ("area/parent.md", "Parent"),
        ("area/deep/subdir/child.md", "Child"),
        ("area/deep/subdir/document żółć.md", "Encoded"),
    ]:
        write_document(tmp_path, relative_path, pending_document(title, f"Body {title}"))
    client = create_app(DocumentationRepository(tmp_path), "Reviewer").test_client()

    response = client.get("/document?path=area/deep/source.md")
    document_links = navigation(response.text).links[1:]

    assert response.status_code == 200
    assert [parse_qs(urlsplit(link).query)[PATH_PARAMETER][0] for link in document_links] == [
        "area/parent.md",
        "area/deep/subdir/child.md",
        "area/deep/subdir/document żółć.md",
    ]
    assert all(client.get(link).status_code == 200 for link in document_links)


def test_markdown_document_link_preserves_script_name(tmp_path: Path) -> None:
    write_document(tmp_path, "source.md", pending_document("Source", "[Target](target.md)"))
    write_document(tmp_path, "target.md", pending_document("Target", "Target body"))
    client = create_app(DocumentationRepository(tmp_path), "Reviewer").test_client()
    request_options = {"environ_overrides": {"SCRIPT_NAME": "/approval"}}

    response = client.get("/document?path=source.md", **request_options)
    target_link = navigation(response.text).links[1]

    assert target_link == "/approval/document?path=target.md"
    assert client.get(target_link.removeprefix("/approval"), **request_options).status_code == 200


def test_fragment_external_mailto_and_non_document_resources_are_not_rewritten(
    tmp_path: Path,
) -> None:
    markdown = (
        "[Section](#section) [Web](https://example.com/a.md) "
        "[Email](mailto:docs@example.com) [Asset](diagram.svg) ![Image](image.png)"
    )

    rendered = render_markdown(
        markdown,
        current_document=Path("source.md"),
        documentation_dir=tmp_path,
        document_url=lambda path: f"preview:{path}",
    )

    assert 'href="#section"' in rendered
    assert 'href="https://example.com/a.md"' in rendered
    assert 'href="mailto:docs@example.com"' in rendered
    assert 'href="diagram.svg"' in rendered
    assert "<img" not in rendered


def test_missing_markdown_document_has_controlled_not_found_page(tmp_path: Path) -> None:
    write_document(tmp_path, "source.md", pending_document("Source", "[Missing](missing.md)"))
    client = create_app(DocumentationRepository(tmp_path), "Reviewer").test_client()

    source_response = client.get("/document?path=source.md")
    missing_link = navigation(source_response.text).links[1]
    missing_response = client.get(missing_link)

    assert missing_link == "/document?path=missing.md"
    assert missing_response.status_code == 404
    assert "Nie znaleziono" in missing_response.text
    assert navigation(missing_response.text).links == ["/"]


@pytest.mark.parametrize(
    "path",
    ["../outside.md", "%2e%2e/outside.md", "%252e%252e/outside.md", "/absolute.md"],
)
def test_preview_route_never_reads_outside_documentation_directory(
    tmp_path: Path, path: str
) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    write_document(tmp_path, "outside.md", pending_document("Secret", "outside secret"))
    client = create_app(DocumentationRepository(docs), "Reviewer").test_client()

    response = client.get(f"/document?path={quote(path, safe='%/')}")

    assert response.status_code == 404
    assert "outside secret" not in response.text


def test_approved_link_target_can_be_read_but_not_approved_again(tmp_path: Path) -> None:
    write_document(tmp_path, "source.md", pending_document("Source", "[Target](target.md)"))
    write_document(
        tmp_path,
        "target.md",
        "---\ntitle: Approved target\napproval_status: approved\n---\n# Approved target\n",
    )
    client = create_app(DocumentationRepository(tmp_path), "Reviewer").test_client()

    source_response = client.get("/document?path=source.md")
    target_response = client.get(navigation(source_response.text).links[1])

    assert target_response.status_code == 200
    assert "Approved target" in target_response.text
    assert navigation(target_response.text).form_actions == []


def test_draft_document_is_not_queued_and_cannot_be_approved(tmp_path: Path) -> None:
    path = write_document(tmp_path, "draft.md", draft_document("Roboczy", "Jeszcze niegotowy."))
    repository = DocumentationRepository(tmp_path)
    client = create_app(repository, "Reviewer").test_client()

    queue_response = client.get("/")
    approval_response = client.post("/approve", data={PATH_PARAMETER: "draft.md"})

    assert repository.pending_documents() == []
    assert "Brak dokumentów oczekujących" in queue_response.text
    assert approval_response.status_code == 400
    assert "Dokument nie oczekuje na akceptację" in approval_response.text
    assert path.read_text(encoding="utf-8") == draft_document("Roboczy", "Jeszcze niegotowy.")


def test_scans_only_documents_explicitly_pending(tmp_path: Path) -> None:
    write_document(
        tmp_path,
        "nested/pending.md",
        "---\ndocument_id: DOC-1\ntitle: Oczekujący\napproval_status: pending\n---\n# Treść\n",
    )
    write_document(tmp_path, "without-status.md", "---\ntitle: Bez statusu\n---\n# Treść\n")
    write_document(
        tmp_path, "approved.md", "---\ntitle: Gotowy\napproval_status: approved\n---\n# Treść\n"
    )
    write_document(tmp_path, "draft.md", draft_document("Roboczy", "Treść robocza"))
    write_document(
        tmp_path,
        "invalid.md",
        "---\ntitle: [niezamknięte\napproval_status: pending\n---\n# Treść\n",
    )

    documents = DocumentationRepository(tmp_path).pending_documents()

    assert [
        (document.document_id, document.title, str(document.relative_path))
        for document in documents
    ] == [("DOC-1", "Oczekujący", "nested/pending.md")]


def test_navigation_links_support_repeated_queue_preview_cycles(tmp_path: Path) -> None:
    app = make_app(tmp_path)
    client = app.test_client()

    queue_response = client.get("/")

    assert queue_response.status_code == 200
    queue_navigation = navigation(queue_response.text)
    assert queue_navigation.links[0] == "/"
    assert len(queue_navigation.links[1:]) == 3
    assert queue_navigation.form_actions == ["/approve"] * 3

    for preview_url in queue_navigation.links[1:]:
        preview_response = client.get(preview_url)
        assert preview_response.status_code == 200
        assert "Akceptuj" in preview_response.text
        assert ".document table { width: 100%; border-collapse: collapse;" in preview_response.text
        assert ".document tbody tr:nth-child(even)" in preview_response.text
        assert ".document tbody tr:hover" in preview_response.text
        assert (
            ".document pre { background: #f6f8fa; border-radius: .375rem;" in preview_response.text
        )

        preview_navigation = navigation(preview_response.text)
        assert preview_navigation.links == ["/"]
        assert preview_navigation.form_actions == ["/approve"]
        assert client.get(preview_navigation.links[0]).status_code == 200


def test_all_generated_application_urls_are_registered_and_directly_accessible(
    tmp_path: Path,
) -> None:
    app = make_app(tmp_path)
    client = app.test_client()

    queue_response = client.get("/")
    queue_navigation = navigation(queue_response.text)

    assert set(rule.endpoint for rule in app.url_map.iter_rules()) >= {
        "queue",
        "document",
        "approve",
    }
    assert all(client.get(url).status_code == 200 for url in queue_navigation.links)
    assert queue_navigation.form_actions == ["/approve"] * 3
    assert queue_navigation.hidden_values == [
        "nested/document-1.md",
        "nested/document-2.md",
        "nested/document-3.md",
    ]
    for preview_url in queue_navigation.links[1:]:
        query = parse_qs(urlsplit(preview_url).query)
        assert query[PATH_PARAMETER]
        preview_navigation = navigation(client.get(preview_url).text)
        assert all(client.get(url).status_code == 200 for url in preview_navigation.links)
        assert preview_navigation.form_actions == ["/approve"]


def test_approval_action_redirects_to_the_named_queue_endpoint(tmp_path: Path) -> None:
    app = make_app(tmp_path, document_count=1)
    client = app.test_client()
    preview_url = navigation(client.get("/").text).links[1]
    preview_response = client.get(preview_url)
    preview_navigation = navigation(preview_response.text)

    approval_response = client.post(
        preview_navigation.form_actions[0],
        data={PATH_PARAMETER: preview_navigation.hidden_values[0]},
    )

    assert approval_response.status_code == 303
    returned_queue = client.get(approval_response.headers["Location"])
    assert returned_queue.status_code == 200
    assert "Zaakceptowano nested/document-1.md" in returned_queue.text
    assert "Brak dokumentów oczekujących" in returned_queue.text


def test_urls_include_script_name_prefix_and_remain_navigable(tmp_path: Path) -> None:
    app = make_app(tmp_path, document_count=2)
    client = app.test_client()
    script_name = "/approval"
    request_options = {"environ_overrides": {"SCRIPT_NAME": script_name}}

    queue_response = client.get("/", **request_options)
    queue_navigation = navigation(queue_response.text)

    assert queue_response.status_code == 200
    assert all(url.startswith(script_name) for url in queue_navigation.links)
    assert all(url.startswith(script_name) for url in queue_navigation.form_actions)
    for preview_url in queue_navigation.links[1:]:
        path_without_prefix = preview_url.removeprefix(script_name)
        preview_response = client.get(path_without_prefix, **request_options)
        assert preview_response.status_code == 200
        preview_navigation = navigation(preview_response.text)
        assert preview_navigation.links == [f"{script_name}/"]
        assert preview_navigation.form_actions == [f"{script_name}/approve"]


def test_markdown_renders_github_style_document_features() -> None:
    markdown = """# Przegląd dokumentu

| Element | Status |
| --- | :---: |
| Tabela | Gotowa |
| Kod | Gotowy |

1. Pierwszy krok
   - element zagnieżdżony
   - [x] wykonane
2. Drugi krok

> Ważna uwaga

---

```python
print("bezpieczny kod")
```

Użyj `inline_code`, odwiedź https://example.com lub [dokumentację](https://example.org/docs).
"""

    rendered = render_markdown(markdown)

    assert '<h1 id="przegląd-dokumentu">Przegląd dokumentu</h1>' in rendered
    assert "<table>" in rendered
    assert "<thead>" in rendered
    assert "<tbody>" in rendered
    assert '<th style="text-align:center;">Status</th>' in rendered
    assert "<ol>" in rendered
    assert '<ul class="contains-task-list">' in rendered
    assert 'class="task-list-item"' in rendered
    assert 'type="checkbox"' in rendered
    assert "checked" in rendered
    assert "disabled" in rendered
    assert "<blockquote>" in rendered
    assert "<hr>" in rendered
    assert '<code class="language-python">' in rendered
    assert "<code>inline_code</code>" in rendered
    assert '<a href="https://example.com">https://example.com</a>' in rendered
    assert '<a href="https://example.org/docs">dokumentację</a>' in rendered


def test_markdown_does_not_allow_arbitrary_html_or_javascript() -> None:
    markdown = """<script>alert("xss")</script>

<img src=x onerror=alert(1)>

[niebezpieczny link](javascript:alert(1))

[bezpieczny link](https://example.com "tytuł")
"""

    rendered = render_markdown(markdown)

    assert "<script" not in rendered
    assert "<img" not in rendered
    assert 'href="javascript:' not in rendered
    assert "&lt;script&gt;" in rendered
    assert "&lt;img src=x onerror=alert(1)&gt;" in rendered
    assert '<a href="https://example.com" title="tytuł">bezpieczny link</a>' in rendered


@pytest.mark.parametrize("trailing_newline", [True, False])
def test_approval_writes_valid_front_matter_without_yaml_end_marker(
    tmp_path: Path, trailing_newline: bool
) -> None:
    body = """# Nagłówek

Wielowierszowa treść z legalnym separatorem YAML:
...

```yaml
...
```

Nie zmieniaj tej treści.
"""
    source = (
        """---
document_id: DOC-1
title: "Tytuł: żółć"
document_type: requirement
status: proposed
version: 1.0
owner: "zespół: dokumentacji"
tags: [alpha, beta]
approval_status: pending
approved_by:
approved_at:
---
"""
        + body
    )
    if not trailing_newline:
        source = source.rstrip("\n")
    path = write_document(tmp_path, "pending.md", source)
    repository = DocumentationRepository(tmp_path)

    repository.approve("pending.md", 'Krzysztof Olejnik: "KGAID"')

    updated = path.read_text(encoding="utf-8")
    updated_front_matter = parse_front_matter(updated)
    source_front_matter = parse_front_matter(source)

    assert updated_front_matter is not None
    assert source_front_matter is not None
    assert updated.startswith("---\n")
    assert updated.count("---\n") == 2
    assert "...\n" not in updated_front_matter.raw
    assert updated_front_matter.body == source_front_matter.body
    assert {
        key: value
        for key, value in updated_front_matter.metadata.items()
        if key not in {"approval_status", "approved_by", "approved_at"}
    } == {
        key: value
        for key, value in source_front_matter.metadata.items()
        if key not in {"approval_status", "approved_by", "approved_at"}
    }
    assert updated_front_matter.metadata["approval_status"] == "approved"
    assert updated_front_matter.metadata["approved_by"] == 'Krzysztof Olejnik: "KGAID"'
    assert "document_type: requirement\n" in updated_front_matter.raw
    assert 'title: "Tytuł: żółć"\n' in updated_front_matter.raw
    assert 'owner: "zespół: dokumentacji"\n' in updated_front_matter.raw
    assert "tags: [alpha, beta]\n" in updated_front_matter.raw
    assert "approval_status: approved\n" in updated_front_matter.raw
    assert "approved_by: 'Krzysztof Olejnik: \"KGAID\"'\n" in updated_front_matter.raw
    approved_at = next(
        line.removeprefix("approved_at: ")
        for line in updated.splitlines()
        if line.startswith("approved_at: ")
    )
    assert datetime.fromisoformat(approved_at).tzinfo is not None
    assert updated_front_matter.metadata["approved_at"] == datetime.fromisoformat(approved_at)
    assert (
        updated_front_matter.raw.replace(
            "approval_status: approved\n", "approval_status: pending\n"
        )
        .replace("approved_by: 'Krzysztof Olejnik: \"KGAID\"'\n", "approved_by:\n")
        .replace(f"approved_at: {approved_at}\n", "approved_at:\n")
        == source_front_matter.raw
    )
    assert repository.pending_documents() == []


def test_invalid_yaml_is_never_overwritten(tmp_path: Path) -> None:
    source = "---\ntitle: [niezamknięte\napproval_status: pending\n---\n# Treść\n"
    path = write_document(tmp_path, "invalid.md", source)
    repository = DocumentationRepository(tmp_path)

    with pytest.raises(ApprovalError, match="Nieprawidłowy YAML"):
        repository.approve("invalid.md", "Krzysztof Olejnik")

    assert path.read_text(encoding="utf-8") == source


def test_cannot_approve_path_outside_documentation_directory(tmp_path: Path) -> None:
    documentation = tmp_path / "docs"
    documentation.mkdir()
    outside = write_document(
        tmp_path,
        "outside.md",
        "---\napproval_status: pending\n---\n# Poza katalogiem\n",
    )
    repository = DocumentationRepository(documentation)

    with pytest.raises(ApprovalError, match="względna|nie znajduje"):
        repository.approve("../outside.md", "Krzysztof Olejnik")

    assert "approval_status: pending" in outside.read_text(encoding="utf-8")
