from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pytest

from kgaid_approval import ApprovalError, DocumentationRepository
from kgaid_approval.web import document_page, queue_page


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
