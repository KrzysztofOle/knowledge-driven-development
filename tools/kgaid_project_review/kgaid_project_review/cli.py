"""Command-line entry point for KGAID project documentation review."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .analysis import ReviewError, analyse_documentation
from .report import json_report, markdown_report

EXIT_OK = 0
EXIT_FINDINGS = 1
EXIT_CONFIGURATION = 2


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(
        description="Generate a read-only KGAID Project Health Report for a documentation directory."
    )
    command.add_argument(
        "--docs-dir", required=True, type=Path, help="Documentation directory to analyse."
    )
    command.add_argument("--output", type=Path, help="Report file; stdout when omitted.")
    command.add_argument(
        "--format", choices=("markdown", "json"), default="markdown", help="Report format."
    )
    command.add_argument(
        "--strict", action="store_true", help="Return failure when warnings are present."
    )
    return command


def _output_inside_docs(docs_dir: Path, output: Path) -> bool:
    try:
        output.resolve().relative_to(docs_dir.resolve())
    except ValueError:
        return False
    return True


def main(argv: list[str] | None = None) -> int:
    command = parser()
    args = command.parse_args(argv)
    try:
        if args.output and _output_inside_docs(args.docs_dir, args.output):
            raise ReviewError("Output file must be outside the analysed documentation directory.")
        report = analyse_documentation(args.docs_dir)
        output = markdown_report(report) if args.format == "markdown" else json_report(report)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(output, encoding="utf-8")
        else:
            sys.stdout.write(output)
    except (ReviewError, OSError) as error:
        command.error(str(error))
        return EXIT_CONFIGURATION
    if report["summary"]["errors"]:
        return EXIT_FINDINGS
    if args.strict and report["summary"]["warnings"]:
        return EXIT_FINDINGS
    return EXIT_OK


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
