from __future__ import annotations

from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from kgaid_approval import ApprovalError, DocumentationRepository
from kgaid_approval.app import create_app
from kgaid_approval.repository import parse_front_matter
from kgaid_approval.routes import PATH_PARAMETER
from kgaid_approval.web import render_markdown


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
