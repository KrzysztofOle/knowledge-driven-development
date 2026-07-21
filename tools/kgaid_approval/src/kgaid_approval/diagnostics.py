"""Runtime diagnostics for identifying an approval-tool installation."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, distribution
from pathlib import Path

_DISTRIBUTION_NAME = "kgaid-documentation-approval"
_UPSTREAM_PATTERN = re.compile(
    r"^(?:[-*]\s*)?(?:upstream\s+)?(?:commit|revision|version|tag|ref)\s*[:=]\s*(.+)$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Diagnostics:
    """Environment values useful when diagnosing which installation is running."""

    version: str
    module_path: Path
    python_executable: Path
    package_location: Path
    working_directory: Path
    docs_root: Path | None = None
    approver: str | None = None
    upstream: str | None = None


def collect_diagnostics(
    *,
    docs_root: Path | None = None,
    approver: str | None = None,
    module_path: Path | None = None,
) -> Diagnostics:
    """Collect diagnostics without invoking Git or any other subprocess."""
    package_location = Path(__file__).resolve().parent
    version, metadata_upstream = _distribution_details()
    return Diagnostics(
        version=version,
        module_path=(module_path or Path(__file__)).resolve(),
        # Keep the virtual-environment entry point instead of resolving its symlink
        # to the base interpreter; that distinction is the point of this diagnostic.
        python_executable=Path(sys.executable).absolute(),
        package_location=package_location,
        working_directory=Path.cwd().resolve(),
        docs_root=docs_root.resolve() if docs_root is not None else None,
        approver=approver,
        upstream=_upstream_from_file(package_location) or metadata_upstream,
    )


def format_cli_diagnostics(diagnostics: Diagnostics) -> str:
    """Format diagnostics for ``kgaid-doc-approval --version``."""
    lines = [
        "KGAID Documentation Approval",
        f"Version: {diagnostics.version}",
        f"Module path: {diagnostics.module_path}",
        f"Python executable: {diagnostics.python_executable}",
        f"Package location: {diagnostics.package_location}",
        f"Working directory: {diagnostics.working_directory}",
    ]
    if diagnostics.upstream:
        lines.append(f"Upstream: {diagnostics.upstream}")
    return "\n".join(lines)


def _distribution_details() -> tuple[str, str | None]:
    try:
        installed_distribution = distribution(_DISTRIBUTION_NAME)
    except PackageNotFoundError:
        return "unknown", None

    upstream = next(
        (
            installed_distribution.metadata.get(key)
            for key in ("VCS-Revision", "Source-Revision", "Commit", "Revision")
            if installed_distribution.metadata.get(key)
        ),
        None,
    )
    try:
        direct_url = json.loads(installed_distribution.read_text("direct_url.json") or "{}")
    except (json.JSONDecodeError, OSError, UnicodeError):
        direct_url = {}
    vcs_info = direct_url.get("vcs_info", {}) if isinstance(direct_url, dict) else {}
    if isinstance(vcs_info, dict):
        upstream = vcs_info.get("commit_id") or vcs_info.get("requested_revision") or upstream
    return installed_distribution.version, upstream


def _upstream_from_file(package_location: Path) -> str | None:
    candidates = (
        package_location / "UPSTREAM.md",
        package_location.parent / "UPSTREAM.md",
        package_location.parent.parent / "UPSTREAM.md",
    )
    for candidate in candidates:
        if not candidate.is_file():
            continue
        try:
            lines = candidate.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError):
            continue
        for line in lines:
            match = _UPSTREAM_PATTERN.match(line.strip())
            if match:
                return match.group(1).strip()
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            value = stripped
            if value:
                return value
    return None
