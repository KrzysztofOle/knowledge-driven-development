"""Stable Markdown and JSON serialisation of a logical project health report."""

from __future__ import annotations

import json
from typing import Any


def json_report(report: dict[str, Any]) -> str:
    """Render the documented JSON representation with stable key ordering."""
    return json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def markdown_report(report: dict[str, Any]) -> str:
    """Render a stable, human-readable projection of the JSON report."""
    summary = report["summary"]
    inventory = report["inventory"]
    lines = [
        "# KGAID Project Health Report",
        "",
        f"- Generated at: {report['generated_at']}",
        f"- Documentation directory: `{report['docs_dir']}`",
        f"- Tool version: {report['tool_version']}",
        f"- KGAID profile: {report['profile']['name']} {report['profile']['version']}",
        "",
        "## Executive Summary",
        "",
        f"- Errors: {summary['errors']}",
        f"- Warnings: {summary['warnings']}",
        f"- Information for review: {summary['info']}",
        "- This report does not establish a baseline, approve documents, or make a Human Authority readiness decision.",
        "",
        "## Inventory",
        "",
        f"- Markdown files found: {inventory['markdown_files']}",
        f"- KGAID-managed documents: {inventory['managed_documents']}",
        f"- Excluded documents: {sum(inventory['excluded_documents'].values())}",
        "",
    ]
    _mapping(lines, "Excluded documents by category", inventory["excluded_documents"])
    _mapping(lines, "Documents by documentation area", inventory["by_area"])
    _mapping(lines, "Documents by document_type", inventory["by_document_type"])
    _mapping(lines, "Documents by status", inventory["by_status"])
    _mapping(lines, "Documents by approval_status", inventory["by_approval_status"])
    _mapping(lines, "Documents by owner", inventory["by_owner"])
    lines.extend(["## Metadata Compliance", ""])
    _findings(lines, report["findings"], prefix="META")
    lines.extend(["## Approval State", "", "### Pending", ""])
    _paths(lines, report["approval"]["pending"])
    lines.extend(["### Approved", ""])
    _paths(lines, report["approval"]["approved"])
    lines.extend(["### Historical statuses (superseded, retired, rejected)", ""])
    _paths(lines, report["approval"]["historical"])
    lines.extend(["## Links", ""])
    _mapping(lines, "Link inventory", report["links"]["counts"])
    lines.extend(["### Valid local links", ""])
    _link_rows(lines, report["links"]["valid"])
    lines.extend(["### Broken local links", ""])
    _link_rows(lines, report["links"]["broken"])
    lines.extend(["### Links outside documentation directory", ""])
    _link_rows(lines, report["links"]["outside"])
    lines.extend(["### Invalid local link paths", ""])
    _link_rows(lines, report["links"]["invalid"])
    lines.extend(["### External links (not fetched)", ""])
    _link_rows(lines, report["links"]["external"])
    lines.extend(["### Link findings", ""])
    _findings(lines, report["findings"], prefix="LINK")
    traceability = report["traceability"]
    lines.extend(
        [
            "## Traceability",
            "",
            f"- Registered document IDs: {len(traceability['registry'])}",
            f"- Detected outgoing references: {traceability['connection_count']}",
            "",
            "### Missing identifier references",
            "",
        ]
    )
    if traceability["unknown_references"]:
        for reference in traceability["unknown_references"]:
            lines.append(f"- `{reference['path']}` → `{reference['identifier']}`")
    else:
        lines.append("- None.")
    lines.extend(["", "### Duplicate identifiers", ""])
    _paths(lines, traceability["duplicate_ids"])
    lines.extend(["### Document connections", ""])
    _connections(lines, report["documents"])
    lines.extend(["### Documents with no detected stable-identifier relationships", ""])
    _paths(lines, traceability["orphaned_documents"])
    lines.extend(["### Traceability findings", ""])
    _findings(lines, report["findings"], prefix="TRACE")
    lines.extend(["## Human Review Required", ""])
    for question in report["human_review_required"]:
        lines.append(f"- {question}")
    lines.extend(
        [
            "",
            "## Findings",
            "",
            "| Code | Severity | Path | Description |",
            "| --- | --- | --- | --- |",
        ]
    )
    for finding in report["findings"]:
        path = finding["path"] or "—"
        lines.append(
            f"| {finding['code']} | {finding['severity']} | `{path}` | {finding['message']} |"
        )
    if not report["findings"]:
        lines.append("| — | — | — | No findings. |")
    return "\n".join(lines) + "\n"


def _mapping(lines: list[str], title: str, values: dict[str, int]) -> None:
    lines.extend([f"### {title}", ""])
    if values:
        for key, value in values.items():
            lines.append(f"- `{key}`: {value}")
    else:
        lines.append("- None.")
    lines.append("")


def _paths(lines: list[str], paths: list[str]) -> None:
    if paths:
        lines.extend(f"- `{path}`" for path in paths)
    else:
        lines.append("- None.")
    lines.append("")


def _link_rows(lines: list[str], links: list[dict[str, str]]) -> None:
    if links:
        for link in links:
            lines.append(f"- `{link['path']}` → `{link['target']}`")
    else:
        lines.append("- None.")
    lines.append("")


def _connections(lines: list[str], documents: list[dict[str, Any]]) -> None:
    if documents:
        for document in documents:
            identifier = document["document_id"] or "<missing>"
            outgoing = ", ".join(document["outgoing_ids"]) or "none"
            incoming = ", ".join(document["incoming_ids"]) or "none"
            lines.append(
                f"- `{document['path']}` (`{identifier}`): outgoing `{outgoing}`; incoming `{incoming}`"
            )
    else:
        lines.append("- None.")
    lines.append("")


def _findings(lines: list[str], findings: list[dict[str, Any]], prefix: str) -> None:
    relevant = [finding for finding in findings if finding["code"].startswith(prefix)]
    if relevant:
        for finding in relevant:
            lines.append(
                f"- `{finding['code']}` ({finding['severity']}) `{finding['path']}` — {finding['message']}"
            )
    else:
        lines.append("- None.")
    lines.append("")
