from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pytest

from kgaid_approval import ApprovalError, DocumentationRepository
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


def test_approval_preserves_existing_yaml_and_markdown_body(tmp_path: Path) -> None:
    source = """---
document_id: DOC-1
title: Tytuł
document_type: requirement
status: proposed
version: 1.0
owner: zespół dokumentacji
tags: [alpha, beta]
approval_status: pending
approved_by:
approved_at:
---
# Nagłówek

Nie zmieniaj tej treści.
"""
    path = write_document(tmp_path, "pending.md", source)
    repository = DocumentationRepository(tmp_path)

    repository.approve("pending.md", "Krzysztof Olejnik")

    updated = path.read_text(encoding="utf-8")
    assert "document_type: requirement\n" in updated
    assert "status: proposed\n" in updated
    assert "version: 1.0\n" in updated
    assert "owner: zespół dokumentacji\n" in updated
    assert "tags: [alpha, beta]\n" in updated
    assert "approval_status: approved\n" in updated
    assert "approved_by: Krzysztof Olejnik\n" in updated
    approved_at = next(
        line.removeprefix("approved_at: ")
        for line in updated.splitlines()
        if line.startswith("approved_at: ")
    )
    assert datetime.fromisoformat(approved_at).tzinfo is not None
    assert updated.split("---\n", 2)[2] == source.split("---\n", 2)[2]
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
