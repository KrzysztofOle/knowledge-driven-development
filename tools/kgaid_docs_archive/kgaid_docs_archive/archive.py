"""ZIP archive creation for a project's documentation."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def archive_name(now: datetime | None = None) -> str:
    """Return the standard archive filename using local time."""
    timestamp = now or datetime.now()
    return f"docs_{timestamp:%Y-%m-%d_%H%M}.zip"


def create_archive(
    root: Path,
    output_dir: Path | None = None,
    now: datetime | None = None,
) -> Path:
    """Archive ``root/docs`` and return the path of the created ZIP file."""
    root = root.resolve()
    docs_dir = root / "docs"
    if not docs_dir.is_dir():
        raise FileNotFoundError(f"Nie znaleziono katalogu dokumentacji: {docs_dir}")

    destination = (output_dir or root).resolve()
    if not destination.is_dir():
        raise NotADirectoryError(f"Katalog docelowy nie istnieje: {destination}")

    archive_path = destination / archive_name(now)
    if archive_path.exists():
        raise FileExistsError(f"Archiwum już istnieje: {archive_path}")

    files = sorted(
        path
        for path in docs_dir.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    )

    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(root))

    return archive_path
