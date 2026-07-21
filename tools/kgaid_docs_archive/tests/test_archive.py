from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

import pytest

from kgaid_docs_archive.archive import archive_name, create_archive


def test_archive_name_uses_required_format() -> None:
    assert archive_name(datetime(2026, 7, 20, 14, 30)) == "docs_2026-07-20_1430.zip"


def test_create_archive_keeps_docs_directory(tmp_path: Path) -> None:
    docs = tmp_path / "docs" / "nested"
    docs.mkdir(parents=True)
    (docs / "guide.md").write_text("# Guide", encoding="utf-8")

    archive_path = create_archive(tmp_path, now=datetime(2026, 7, 20, 14, 30))

    assert archive_path.name == "docs_2026-07-20_1430.zip"
    with ZipFile(archive_path) as archive:
        assert archive.namelist() == ["docs/nested/guide.md"]


def test_create_archive_requires_docs_directory(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        create_archive(tmp_path)


def test_create_archive_does_not_overwrite_existing_file(tmp_path: Path) -> None:
    (tmp_path / "docs").mkdir()
    created_at = datetime(2026, 7, 20, 14, 30)
    create_archive(tmp_path, now=created_at)

    with pytest.raises(FileExistsError):
        create_archive(tmp_path, now=created_at)
