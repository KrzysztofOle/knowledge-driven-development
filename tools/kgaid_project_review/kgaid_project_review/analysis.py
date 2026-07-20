"""Read-only discovery and conservative analysis of a documentation directory."""

from __future__ import annotations

import os
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, TypedDict

import yaml

from . import profile

MARKDOWN_SUFFIXES = frozenset({".md", ".markdown"})
TECHNICAL_DIRECTORIES = frozenset(
    {
        ".git",
        ".hg",
        ".svn",
        ".venv",
        "venv",
        "node_modules",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "build",
        "dist",
    }
)
EXCLUDED_DIRECTORY_CATEGORIES = {
    "template": frozenset({"template", "templates"}),
    "staging": frozenset({"staging", "knowledge-staging"}),
    "working-report": frozenset({"working-reports", "working-report", "reports-working"}),
}
HISTORICAL_STATUSES = frozenset({"superseded", "retired", "rejected"})
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^#\s+(.+?)\s*#*\s*$")
HEADING_IDENTIFIER_PREFIX = re.compile(r"^[A-Z][A-Z0-9]{1,}(?:-[A-Z][A-Z0-9]*)*-\d{3,}\s+[—-]\s+")
# Stable-document identifiers use an upper-case family and at least a three-digit serial,
# e.g. REQ-001 or KGAID-ARCH-014. This intentionally excludes prose such as KG-1.
IDENTIFIER_PATTERN = re.compile(
    r"(?<![A-Z0-9-])[A-Z][A-Z0-9]{1,}(?:-[A-Z][A-Z0-9]*)*-\d{3,}(?![A-Z0-9-])"
)


class ReviewError(Exception):
    """Raised for invalid or inaccessible review input."""


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    path: str | None
    message: str


@dataclass
class DocumentRecord:
    path: str
    exclusion_category: str | None
    metadata: dict[str, str]
    body: str
    document_id: str | None
    links: list[dict[str, str]]
    outgoing_ids: list[str]

    @property
    def managed(self) -> bool:
        return self.exclusion_category is None


class DocumentRow(TypedDict):
    path: str
    document_id: str | None
    document_type: str | None
    status: str | None
    approval_status: str | None
    owner: str | None
    outgoing_ids: list[str]
    incoming_ids: list[str]


def _inside(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
    except ValueError:
        return False
    return True


def _exclusion_category(relative: Path) -> str | None:
    name = relative.name.lower()
    if name == "readme.md":
        return "navigation-readme"
    if name == "agents.md":
        return "instructions"
    parents = {part.lower() for part in relative.parts[:-1]}
    for category, directories in EXCLUDED_DIRECTORY_CATEGORIES.items():
        if parents & directories:
            return category
    if name.endswith("-working-report.md"):
        return "working-report"
    return None


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ReviewError(f"Cannot read documentation file {path}: {error}") from error


def _split_front_matter(text: str) -> tuple[dict[str, Any] | None, str, str | None]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        return None, text, "missing"
    end_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.rstrip("\r\n") in {"---", "..."}:
            end_index = index
            break
    if end_index is None:
        return None, text, "unterminated"
    raw = "".join(lines[1:end_index])
    try:
        metadata = yaml.load(raw, Loader=profile.DuplicateKeySafeLoader)
    except yaml.YAMLError as error:
        return None, "".join(lines[end_index + 1 :]), str(error)
    if not isinstance(metadata, dict) or not all(isinstance(key, str) for key in metadata):
        return (
            None,
            "".join(lines[end_index + 1 :]),
            "front matter must be a mapping with text keys",
        )
    return metadata, "".join(lines[end_index + 1 :]), None


def _without_fenced_code(text: str) -> str:
    kept: list[str] = []
    marker: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        fence = re.match(r"(`{3,}|~{3,})", stripped)
        if fence:
            current = fence.group(1)[0]
            if marker is None:
                marker = current
            elif marker == current:
                marker = None
            continue
        if marker is None:
            kept.append(line)
    return "\n".join(kept)


def _first_h1(body: str) -> str | None:
    for line in _without_fenced_code(body).splitlines():
        if match := HEADING_PATTERN.match(line):
            return match.group(1).strip()
    return None


def _title_matches_heading(title: str, heading: str) -> bool:
    """Accept the common ``ID — Title`` H1 convention without weakening comparison."""
    return title == heading or title == HEADING_IDENTIFIER_PREFIX.sub("", heading)


def _link_target(raw_target: str) -> str:
    value = raw_target.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")].strip()
    return value.split(maxsplit=1)[0] if value else ""


def _is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:")) or target.startswith("//")


def _links(body: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for raw in LINK_PATTERN.findall(_without_fenced_code(body)):
        target = _link_target(raw)
        if not target:
            continue
        result.append({"target": target, "kind": "external" if _is_external(target) else "local"})
    return result


def _normalised_metadata(metadata: dict[str, Any]) -> dict[str, str]:
    return {key: profile.metadata_string(value).strip() for key, value in metadata.items()}


def _find(findings: list[Finding], code: str, severity: str, path: str, message: str) -> None:
    findings.append(Finding(code=code, severity=severity, path=path, message=message))


def _validate_metadata(
    record: DocumentRecord, raw: dict[str, Any] | None, error: str | None, findings: list[Finding]
) -> None:
    if error == "missing":
        _find(findings, "META001", "error", record.path, "Missing YAML front matter.")
        return
    if error:
        _find(findings, "META002", "error", record.path, f"Invalid YAML front matter: {error}")
        return
    assert raw is not None
    missing = sorted(profile.REQUIRED_FIELDS - raw.keys())
    if missing:
        _find(
            findings,
            "META003",
            "error",
            record.path,
            f"Missing required fields: {', '.join(missing)}.",
        )
    title = record.metadata.get("title", "")
    if not title:
        _find(findings, "META003", "error", record.path, "Required field title is empty.")
    heading = _first_h1(record.body)
    if title and heading and not _title_matches_heading(title, heading):
        _find(
            findings,
            "META004",
            "warning",
            record.path,
            "Metadata title differs from the first H1 heading.",
        )
    controlled = (
        ("document_type", profile.DOCUMENT_TYPES, "META005"),
        ("status", profile.STATUSES, "META006"),
        ("owner", profile.OWNERS, "META008"),
        ("approval_status", profile.APPROVAL_STATUSES, "META009"),
    )
    for field, vocabulary, code in controlled:
        value = record.metadata.get(field, "")
        if value and value not in vocabulary:
            _find(findings, code, "error", record.path, f"Unsupported {field}: {value!r}.")
        elif field in raw and not value:
            _find(findings, code, "error", record.path, f"{field} must not be empty.")
    if "version" in raw and not profile.is_valid_version(raw["version"]):
        _find(
            findings,
            "META007",
            "error",
            record.path,
            "Version must be numeric (for example 1, 1.0 or 1.0.0).",
        )
    approval_status = record.metadata.get("approval_status", "")
    approved_by = record.metadata.get("approved_by", "")
    approved_at = record.metadata.get("approved_at", "")
    if approval_status == "pending" and (approved_by or approved_at):
        _find(
            findings,
            "META010",
            "error",
            record.path,
            "Pending approval requires empty approved_by and approved_at.",
        )
    if approval_status == "approved":
        if not approved_by or not approved_at:
            _find(
                findings,
                "META011",
                "error",
                record.path,
                "Approved document requires approved_by and approved_at.",
            )
        elif not profile.is_valid_iso8601(raw.get("approved_at")):
            _find(
                findings,
                "META012",
                "error",
                record.path,
                "approved_at must be an ISO 8601 date or timestamp.",
            )


def _scan_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    for current, directories, filenames in os.walk(root, followlinks=False):
        directories[:] = sorted(
            directory for directory in directories if directory not in TECHNICAL_DIRECTORIES
        )
        current_path = Path(current)
        for filename in sorted(filenames):
            path = current_path / filename
            if path.suffix.lower() in MARKDOWN_SUFFIXES and path.is_file():
                resolved = path.resolve()
                if _inside(root, resolved):
                    paths.append(resolved)
    return sorted(paths, key=lambda path: path.relative_to(root).as_posix())


def _analyse_links(
    root: Path, documents: list[DocumentRecord], findings: list[Finding]
) -> dict[str, Any]:
    counts: Counter[str] = Counter()
    links: dict[str, list[dict[str, str]]] = defaultdict(list)
    for document in documents:
        if not document.managed:
            continue
        source = root / document.path
        for link in document.links:
            if link["kind"] == "external":
                counts["external"] += 1
                links["external"].append({"path": document.path, "target": link["target"]})
                continue
            target = link["target"]
            destination, _, _anchor = target.partition("#")
            if not destination:
                counts["valid"] += 1
                links["valid"].append({"path": document.path, "target": target})
                continue
            try:
                candidate = (source.parent / destination).resolve()
            except (OSError, ValueError):
                counts["invalid"] += 1
                links["invalid"].append({"path": document.path, "target": target})
                _find(
                    findings,
                    "LINK003",
                    "error",
                    document.path,
                    f"Invalid local link path: {target!r}.",
                )
                continue
            if not _inside(root, candidate):
                counts["outside"] += 1
                links["outside"].append({"path": document.path, "target": target})
                _find(
                    findings,
                    "LINK002",
                    "error",
                    document.path,
                    f"Link leaves docs directory: {target!r}.",
                )
            elif not candidate.is_file():
                counts["broken"] += 1
                links["broken"].append({"path": document.path, "target": target})
                _find(
                    findings,
                    "LINK001",
                    "error",
                    document.path,
                    f"Missing local link target: {target!r}.",
                )
            else:
                counts["valid"] += 1
                links["valid"].append({"path": document.path, "target": target})
    return {
        "counts": dict(sorted(counts.items())),
        "valid": sorted(links["valid"], key=lambda item: (item["path"], item["target"])),
        "broken": sorted(links["broken"], key=lambda item: (item["path"], item["target"])),
        "outside": sorted(links["outside"], key=lambda item: (item["path"], item["target"])),
        "invalid": sorted(links["invalid"], key=lambda item: (item["path"], item["target"])),
        "external": sorted(links["external"], key=lambda item: (item["path"], item["target"])),
    }


def _sort_findings(findings: list[Finding]) -> list[Finding]:
    severity_order = {"error": 0, "warning": 1, "info": 2}
    return sorted(
        findings,
        key=lambda finding: (
            severity_order[finding.severity],
            finding.code,
            finding.path or "",
            finding.message,
        ),
    )


def analyse_documentation(
    docs_dir: str | Path, generated_at: datetime | None = None
) -> dict[str, Any]:
    """Return a deterministic logical report without modifying ``docs_dir``."""
    supplied = Path(docs_dir).expanduser()
    if not supplied.exists():
        raise ReviewError(f"Documentation directory does not exist: {supplied}")
    if not supplied.is_dir():
        raise ReviewError(f"Documentation path is not a directory: {supplied}")
    try:
        root = supplied.resolve(strict=True)
        next(root.iterdir(), None)
    except OSError as error:
        raise ReviewError(
            f"Documentation directory is not accessible: {supplied}: {error}"
        ) from error

    findings: list[Finding] = []
    documents: list[DocumentRecord] = []
    for path in _scan_files(root):
        relative = path.relative_to(root).as_posix()
        category = _exclusion_category(Path(relative))
        text = _read_text(path)
        raw, body, front_matter_error = _split_front_matter(text)
        metadata = _normalised_metadata(raw) if raw is not None else {}
        record = DocumentRecord(
            path=relative,
            exclusion_category=category,
            metadata=metadata,
            body=body,
            document_id=metadata.get("document_id") or None,
            links=_links(body),
            outgoing_ids=sorted(set(IDENTIFIER_PATTERN.findall(_without_fenced_code(body)))),
        )
        documents.append(record)
        if record.managed:
            _validate_metadata(record, raw, front_matter_error, findings)

    managed = [document for document in documents if document.managed]
    identifiers: dict[str, list[DocumentRecord]] = defaultdict(list)
    for document in managed:
        if document.document_id:
            identifiers[document.document_id].append(document)
    for identifier, matches in sorted(identifiers.items()):
        if len(matches) > 1:
            for match in matches:
                _find(
                    findings,
                    "META013",
                    "error",
                    match.path,
                    f"Duplicate document_id: {identifier}.",
                )
                _find(
                    findings,
                    "TRACE002",
                    "error",
                    match.path,
                    f"Duplicate traceability identifier: {identifier}.",
                )

    link_data = _analyse_links(root, documents, findings)
    known_ids = set(identifiers)
    incoming: dict[str, set[str]] = defaultdict(set)
    unknown_references: list[dict[str, str]] = []
    for document in managed:
        own_id = document.document_id
        for identifier in document.outgoing_ids:
            if identifier == own_id:
                continue
            if identifier in known_ids:
                incoming[identifier].add(document.path)
            else:
                unknown_references.append({"path": document.path, "identifier": identifier})
                _find(
                    findings,
                    "TRACE001",
                    "warning",
                    document.path,
                    f"Referenced document_id does not exist: {identifier}.",
                )
    orphaned: list[str] = []
    for document in managed:
        connections = set(document.outgoing_ids)
        if document.document_id:
            connections.update(incoming.get(document.document_id, set()))
        if not connections:
            orphaned.append(document.path)
            _find(
                findings,
                "TRACE003",
                "info",
                document.path,
                "No stable-identifier links detected; human review is required.",
            )

    exclusions = Counter(
        document.exclusion_category for document in documents if document.exclusion_category
    )
    identifiers_by_path = {document.path: document.document_id for document in managed}
    document_rows: list[DocumentRow] = []
    for document in managed:
        incoming_ids: list[str] = []
        for source in incoming.get(document.document_id or "", set()):
            source_document_id: str | None = identifiers_by_path[source]
            if source_document_id is not None:
                incoming_ids.append(source_document_id)
        document_rows.append(
            {
                "path": document.path,
                "document_id": document.document_id,
                "document_type": document.metadata.get("document_type"),
                "status": document.metadata.get("status"),
                "approval_status": document.metadata.get("approval_status"),
                "owner": document.metadata.get("owner"),
                "outgoing_ids": document.outgoing_ids,
                "incoming_ids": sorted(incoming_ids),
            }
        )
    document_rows.sort(key=lambda item: item["path"])
    finding_rows = [asdict(finding) for finding in _sort_findings(findings)]
    severity_counts = Counter(finding["severity"] for finding in finding_rows)
    inventory = {
        "markdown_files": len(documents),
        "managed_documents": len(managed),
        "excluded_documents": {category: exclusions[category] for category in sorted(exclusions)},
        "by_area": _group(
            managed, lambda item: item.path.split("/", 1)[0] if "/" in item.path else "."
        ),
        "by_document_type": _group(
            managed, lambda item: item.metadata.get("document_type", "<missing>")
        ),
        "by_status": _group(managed, lambda item: item.metadata.get("status", "<missing>")),
        "by_approval_status": _group(
            managed, lambda item: item.metadata.get("approval_status", "<missing>")
        ),
        "by_owner": _group(managed, lambda item: item.metadata.get("owner", "<missing>")),
    }
    now = generated_at or datetime.now(timezone.utc)
    return {
        "schema_version": "1.0",
        "generated_at": now.astimezone(timezone.utc).isoformat(timespec="seconds"),
        "docs_dir": str(root),
        "tool_version": "0.1.0",
        "profile": {"name": profile.PROFILE_NAME, "version": profile.PROFILE_VERSION},
        "summary": {
            "errors": severity_counts["error"],
            "warnings": severity_counts["warning"],
            "info": severity_counts["info"],
        },
        "inventory": inventory,
        "documents": document_rows,
        "approval": {
            "pending": [
                row["path"] for row in document_rows if row["approval_status"] == "pending"
            ],
            "approved": [
                row["path"] for row in document_rows if row["approval_status"] == "approved"
            ],
            "historical": [
                row["path"] for row in document_rows if row["status"] in HISTORICAL_STATUSES
            ],
        },
        "links": link_data,
        "traceability": {
            "registry": sorted(identifiers),
            "unknown_references": sorted(
                unknown_references, key=lambda item: (item["path"], item["identifier"])
            ),
            "duplicate_ids": sorted(
                identifier for identifier, matches in identifiers.items() if len(matches) > 1
            ),
            "orphaned_documents": sorted(orphaned),
            "connection_count": sum(len(row["outgoing_ids"]) for row in document_rows),
        },
        "human_review_required": [
            "Is the product scope complete?",
            "Is the content materially coherent and correct?",
            "Are acceptance criteria sufficient?",
            "Is the project ready for its next stage?",
            "May a human authority establish a baseline?",
            "What should the next priority be?",
        ],
        "findings": finding_rows,
    }


def _group(documents: list[DocumentRecord], key: Callable[[DocumentRecord], str]) -> dict[str, int]:
    values = Counter(key(document) for document in documents)
    return {value: values[value] for value in sorted(values)}
