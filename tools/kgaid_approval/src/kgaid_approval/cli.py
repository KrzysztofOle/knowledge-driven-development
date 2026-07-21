"""Command-line entry point for the local KGAID approval interface."""

from __future__ import annotations

import argparse
from pathlib import Path

from .app import create_app
from .diagnostics import collect_diagnostics, format_cli_diagnostics
from .repository import ApprovalError, DocumentationRepository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lokalna kolejka akceptacji dokumentacji KGAID.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--version",
        action="version",
        version=format_cli_diagnostics(collect_diagnostics(module_path=Path(__file__))),
    )
    parser.add_argument(
        "--docs-dir", type=Path, required=True, help="Katalog dokumentacji do przeglądu."
    )
    parser.add_argument("--approver", required=True, help="Imię i nazwisko osoby zatwierdzającej.")
    parser.add_argument(
        "--host", default="127.0.0.1", help="Adres lokalnego interfejsu (domyślnie 127.0.0.1)."
    )
    parser.add_argument(
        "--port", type=int, default=8765, help="Port lokalnego interfejsu (domyślnie 8765)."
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        repository = DocumentationRepository(args.docs_dir)
    except ApprovalError as error:
        raise SystemExit(f"Błąd konfiguracji: {error}") from error
    app = create_app(repository, args.approver)
    print(f"KGAID Documentation Approval: http://{args.host}:{args.port}")
    app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
