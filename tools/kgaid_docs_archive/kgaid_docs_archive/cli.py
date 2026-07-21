"""Command-line interface for documentation archiving."""

from __future__ import annotations

import argparse
from pathlib import Path

from .archive import create_archive


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(
        description="Tworzy archiwum ZIP katalogu docs/ z nazwą zawierającą datę i czas."
    )
    command.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Katalog główny projektu (domyślnie: bieżący).",
    )
    command.add_argument(
        "--output-dir",
        type=Path,
        help="Katalog zapisu archiwum (domyślnie: katalog projektu).",
    )
    return command


def main() -> None:
    args = parser().parse_args()
    try:
        archive_path = create_archive(args.root, args.output_dir)
    except (FileNotFoundError, NotADirectoryError, FileExistsError) as error:
        parser().error(str(error))
    print(archive_path)
