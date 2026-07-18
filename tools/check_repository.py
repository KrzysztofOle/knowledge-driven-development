#!/usr/bin/env python3
"""Offline repository controls for the prepared KGAID baseline."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/50-governance/baselines/KGAID-0.1.0.yaml"
REQUIRED_FILES = [
    "CONTRIBUTING.md", "CHANGELOG.md", "SECURITY.md", "CODE_OF_CONDUCT.md",
    "CITATION.cff", "LICENSE", "docs/50-governance/governance-and-release-model.md",
    "docs/50-governance/metadata-profile.md",
]
REQUIRED_METADATA = {
    "document_id", "title", "status", "version", "baseline", "normative",
    "maintainer", "last_reviewed", "dependencies", "supersedes", "superseded_by",
    "verification_status", "change_control",
}
VALID_VERIFICATION = {
    "not-planned", "planned", "in-progress", "partially-supported", "failed",
    "verified", "verified-with-limitations", "inconclusive", "invalidated", "expired",
}


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML front matter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def list_value(value: str) -> list[str]:
    if not (value.startswith("[") and value.endswith("]")):
        raise ValueError("expected bracket list")
    body = value[1:-1].strip()
    return [] if not body else [part.strip() for part in body.split(",")]


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
        deps = [item.strip() for item in dependencies.group(1).split(",") if item.strip()]
        result[identifier.group(1).strip()] = (ROOT / path.group(1).strip(), deps)
    return result


def check_links(errors: list[str]) -> None:
    markdown_link = re.compile(r"(?<!!)\[[^]]*\]\(([^)]+)\)")
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        for target in markdown_link.findall(source.read_text(encoding="utf-8")):
            target = target.strip().split(" ", 1)[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if target and not (source.parent / target).resolve().exists():
                errors.append(f"broken internal link in {source.relative_to(ROOT)}: {target}")


def check_dependency_cycles(documents: dict[str, tuple[Path, list[str]]], errors: list[str]) -> None:
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
        errors.append(f"manifest must list 14 normative documents; found {len(documents)}")

    for identifier, (path, manifest_dependencies) in documents.items():
        if not path.is_file():
            errors.append(f"manifest path is missing for {identifier}: {path.relative_to(ROOT)}")
            continue
        try:
            metadata = front_matter(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        missing = REQUIRED_METADATA - metadata.keys()
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing metadata: {', '.join(sorted(missing))}")
        if metadata.get("document_id") != identifier:
            errors.append(f"{path.relative_to(ROOT)} document_id does not match manifest")
        if metadata.get("status") != "Accepted" or metadata.get("normative") != "true":
            errors.append(f"{path.relative_to(ROOT)} is not an Accepted normative document")
        if metadata.get("baseline") != "KGAID-0.1.0" or metadata.get("version") != "0.1.0":
            errors.append(f"{path.relative_to(ROOT)} has inconsistent baseline or version")
        if metadata.get("verification_status") not in VALID_VERIFICATION:
            errors.append(f"{path.relative_to(ROOT)} has invalid verification_status")
        try:
            if list_value(metadata.get("dependencies", "")) != manifest_dependencies:
                errors.append(f"{path.relative_to(ROOT)} dependencies do not match manifest")
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)} has invalid dependencies metadata")

        body = path.read_text(encoding="utf-8")
        if re.search(r"\b(?:KDD|Knowledge-Driven Development)\b", body, re.IGNORECASE):
            errors.append(f"legacy KDD name in normative document: {path.relative_to(ROOT)}")
        if re.search(r"\b(?:must|should|may)\b", body):
            errors.append(f"lower-case normative keyword in {path.relative_to(ROOT)}")

    principles = (ROOT / "docs/00-foundations/02-principles.md").read_text(encoding="utf-8")
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
                errors.append(f"canonical verification status {status} missing from {path.relative_to(ROOT)}")
    legacy_statuses = ("partially-verified", "unverified", "not-required", "| **limited**")
    for path in (ROOT / "docs").rglob("*.md"):
        if path.name.startswith("AUD-"):
            continue
        content = path.read_text(encoding="utf-8")
        for legacy in legacy_statuses:
            if legacy in content:
                errors.append(f"legacy verification status {legacy!r} in {path.relative_to(ROOT)}")

    if errors:
        print("Repository controls failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Repository controls passed: {len(documents)} normative documents checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
