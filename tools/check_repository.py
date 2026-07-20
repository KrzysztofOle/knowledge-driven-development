#!/usr/bin/env python3
"""Offline repository controls for the prepared KGAID baseline."""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "kgaid_project_review"))

from kgaid_project_review.profile import (  # noqa: E402
    APPROVAL_STATUSES as VALID_APPROVAL_STATUSES,
    DOCUMENT_TYPES as VALID_DOCUMENT_TYPES,
    OWNERS as VALID_OWNERS,
    REQUIRED_FIELDS as REQUIRED_METADATA,
    STATUSES as VALID_STATUSES,
    is_valid_version,
)

MANIFEST = ROOT / "docs/50-governance/baselines/KGAID-0.1.0.yaml"
REQUIRED_FILES = [
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "CITATION.cff",
    "LICENSE",
    "docs/50-governance/governance-and-release-model.md",
    "docs/50-governance/metadata-profile.md",
]
VALID_VERIFICATION = {
    "not-planned",
    "planned",
    "in-progress",
    "partially-supported",
    "failed",
    "verified",
    "verified-with-limitations",
    "inconclusive",
    "invalidated",
    "expired",
}


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML front matter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        field = re.fullmatch(r"([a-z][a-z0-9_]*):(?:[ ](.*))?", line)
        if not field:
            raise ValueError(f"invalid front matter line: {line!r}")
        key, value = field.group(1), field.group(2) or ""
        if key in values:
            raise ValueError(f"duplicate front matter field: {key}")
        values[key] = value
    return values


def managed_markdown_documents() -> list[Path]:
    return sorted(
        path for path in (ROOT / "docs").rglob("*.md") if path.name != "README.md"
    )


def check_governed_metadata(errors: list[str]) -> None:
    identifiers: dict[str, Path] = {}
    for path in managed_markdown_documents():
        relative = path.relative_to(ROOT)
        try:
            metadata = front_matter(path)
        except ValueError as error:
            errors.append(f"{relative}: {error}")
            continue

        missing = REQUIRED_METADATA - metadata.keys()
        unexpected = metadata.keys() - REQUIRED_METADATA
        if missing:
            errors.append(f"{relative} missing metadata: {', '.join(sorted(missing))}")
        if unexpected:
            errors.append(
                f"{relative} has non-standard metadata: {', '.join(sorted(unexpected))}"
            )

        identifier = metadata.get("document_id", "")
        if not identifier:
            errors.append(f"{relative} has empty document_id")
        elif identifier in identifiers:
            errors.append(
                f"duplicate document_id {identifier}: "
                f"{identifiers[identifier].relative_to(ROOT)} and {relative}"
            )
        else:
            identifiers[identifier] = path

        if not metadata.get("title"):
            errors.append(f"{relative} has empty title")
        if metadata.get("document_type") not in VALID_DOCUMENT_TYPES:
            errors.append(f"{relative} has invalid document_type")
        if metadata.get("status") not in VALID_STATUSES:
            errors.append(f"{relative} has invalid status")
        if not is_valid_version(metadata.get("version", "")):
            errors.append(f"{relative} has invalid version")
        if metadata.get("owner") not in VALID_OWNERS:
            errors.append(f"{relative} has invalid owner")

        approval_status = metadata.get("approval_status")
        approved_by = metadata.get("approved_by", "")
        approved_at = metadata.get("approved_at", "")
        if approval_status not in VALID_APPROVAL_STATUSES:
            errors.append(f"{relative} has invalid approval_status")
        elif approval_status == "pending" and (approved_by or approved_at):
            errors.append(f"{relative} has approval details while pending")
        elif approval_status == "approved":
            if not approved_by or not approved_at:
                errors.append(f"{relative} has incomplete approval details")
            else:
                try:
                    datetime.fromisoformat(approved_at)
                except ValueError:
                    errors.append(f"{relative} has invalid approved_at ISO 8601 value")


def manifest_documents() -> dict[str, tuple[Path, list[str]]]:
    result: dict[str, tuple[Path, list[str]]] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.startswith("  - { id:"):
            continue
        identifier = re.search(r"id: ([^,}]+)", line)
        path = re.search(r"path: ([^,}]+)", line)
        dependencies = re.search(r"dependencies: \[([^]]*)\]", line)
        if not (identifier and path and dependencies):
            raise ValueError(f"invalid manifest entry: {line}")
        deps = [
            item.strip() for item in dependencies.group(1).split(",") if item.strip()
        ]
        result[identifier.group(1).strip()] = (ROOT / path.group(1).strip(), deps)
    return result


def check_links(errors: list[str]) -> None:
    markdown_link = re.compile(r"(?<!!)\[[^]]*\]\(([^)]+)\)")
    for source in ROOT.rglob("*.md"):
        if {".git", ".venv", "venv", "node_modules", "__pycache__"} & set(source.parts):
            continue
        for target in markdown_link.findall(source.read_text(encoding="utf-8")):
            target = target.strip().split(" ", 1)[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if target and not (source.parent / target).resolve().exists():
                errors.append(
                    f"broken internal link in {source.relative_to(ROOT)}: {target}"
                )


def check_dependency_cycles(
    documents: dict[str, tuple[Path, list[str]]], errors: list[str]
) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(identifier: str) -> None:
        if identifier in visiting:
            errors.append(f"dependency cycle includes {identifier}")
            return
        if identifier in visited:
            return
        visiting.add(identifier)
        for dependency in documents[identifier][1]:
            if dependency not in documents:
                errors.append(f"{identifier} has unknown dependency {dependency}")
            else:
                visit(dependency)
        visiting.remove(identifier)
        visited.add(identifier)

    for identifier in documents:
        visit(identifier)


def main() -> int:
    errors: list[str] = []
    for required in REQUIRED_FILES:
        if not (ROOT / required).is_file():
            errors.append(f"required file is missing: {required}")

    try:
        documents = manifest_documents()
    except ValueError as error:
        errors.append(str(error))
        documents = {}
    if len(documents) != 14:
        errors.append(
            f"manifest must list 14 normative documents; found {len(documents)}"
        )

    check_governed_metadata(errors)

    for identifier, (path, manifest_dependencies) in documents.items():
        if not path.is_file():
            errors.append(
                f"manifest path is missing for {identifier}: {path.relative_to(ROOT)}"
            )
            continue
        try:
            metadata = front_matter(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        if metadata.get("document_id") != identifier:
            errors.append(
                f"{path.relative_to(ROOT)} document_id does not match manifest"
            )
        if metadata.get("status") != "accepted":
            errors.append(
                f"{path.relative_to(ROOT)} is not an Accepted normative document"
            )
        if metadata.get("version") != "0.1.0":
            errors.append(f"{path.relative_to(ROOT)} has inconsistent version")

        body = path.read_text(encoding="utf-8")
        if re.search(r"\b(?:KDD|Knowledge-Driven Development)\b", body, re.IGNORECASE):
            errors.append(
                f"legacy KDD name in normative document: {path.relative_to(ROOT)}"
            )
        if re.search(r"\b(?:must|should|may)\b", body):
            errors.append(f"lower-case normative keyword in {path.relative_to(ROOT)}")

    principles = (ROOT / "docs/00-foundations/02-principles.md").read_text(
        encoding="utf-8"
    )
    for keyword in ("**MUST**", "**SHOULD**", "**MAY**"):
        if keyword not in principles:
            errors.append(f"KGAID Principles does not define {keyword}")

    check_dependency_cycles(documents, errors)
    check_links(errors)

    for path in [
        ROOT / "docs/10-knowledge-architecture/12-artifact-model.md",
        ROOT / "docs/20-methodology/24-delivery-increment-model.md",
        ROOT / "docs/30-quality/31-verification-and-evidence-model.md",
    ]:
        content = path.read_text(encoding="utf-8")
        for status in VALID_VERIFICATION:
            if status not in content:
                errors.append(
                    f"canonical verification status {status} missing from {path.relative_to(ROOT)}"
                )
    legacy_statuses = (
        "partially-verified",
        "unverified",
        "not-required",
        "| **limited**",
    )
    for path in (ROOT / "docs").rglob("*.md"):
        if path.name.startswith("AUD-"):
            continue
        content = path.read_text(encoding="utf-8")
        for legacy in legacy_statuses:
            if legacy in content:
                errors.append(
                    f"legacy verification status {legacy!r} in {path.relative_to(ROOT)}"
                )

    if errors:
        print("Repository controls failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(
        "Repository controls passed: "
        f"{len(managed_markdown_documents())} governed Markdown documents and "
        f"{len(documents)} normative baseline documents checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
