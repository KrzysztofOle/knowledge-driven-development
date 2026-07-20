from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pytest

from kgaid_approval import ApprovalError, DocumentationRepository
from kgaid_approval.repository import parse_front_matter
from kgaid_approval.web import document_page, queue_page, render_markdown


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


def test_preview_includes_document_content_and_approval_action(tmp_path: Path) -> None:
    write_document(
        tmp_path,
        "pending.md",
        "---\ndocument_id: DOC-1\ntitle: Tytuł dokumentu\napproval_status: pending\n---\n# Nagłówek\n\nTreść **do przeglądu**.\n",
    )
    repository = DocumentationRepository(tmp_path)
    document = repository.pending_document("pending.md")

    preview = document_page(document)
    queue = queue_page(repository.pending_documents())

    assert "Nagłówek" in preview
    assert "Akceptuj" in preview
    assert "pending.md" in preview
    assert "Podgląd" in queue
    assert "Akceptuj" in queue
    assert ".document table { width: 100%; border-collapse: collapse;" in preview
    assert ".document tbody tr:nth-child(even)" in preview
    assert ".document tbody tr:hover" in preview
    assert ".document pre { background: #f6f8fa; border-radius: .375rem;" in preview


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
