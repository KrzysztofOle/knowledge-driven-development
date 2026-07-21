"""Canonical, executable KGAID governed-document metadata profile.

The values in this module implement the profile documented in
``docs/50-governance/metadata-profile.md``.  It is deliberately small so local
repository controls and reusable tooling use one vocabulary rather than copy it.
"""

from __future__ import annotations

import re
from datetime import date, datetime
from typing import Any

import yaml

PROFILE_NAME = "KGAID governed document metadata profile"
PROFILE_VERSION = "0.1.0"

REQUIRED_FIELDS = frozenset(
    {
        "document_id",
        "title",
        "document_type",
        "status",
        "version",
        "owner",
        "approval_status",
        "approved_by",
        "approved_at",
    }
)
DOCUMENT_TYPES = frozenset(
    {
        "vision",
        "capability",
        "business-process",
        "business-rule",
        "requirement",
        "glossary",
        "domain-model",
        "adr",
        "architecture",
        "contract",
        "verification",
        "operations",
        "governance",
        "knowledge",
    }
)
STATUSES = frozenset({"draft", "proposed", "accepted", "deprecated", "superseded"})
OWNERS = frozenset({"Product", "Business", "Architecture", "Quality", "Operations", "Governance"})
APPROVAL_STATUSES = frozenset({"draft", "pending", "approved"})
VERSION_PATTERN = re.compile(r"[0-9]+(?:\.[0-9]+){0,2}\Z")


class DuplicateKeySafeLoader(yaml.SafeLoader):
    """Safe YAML loader that refuses ambiguous duplicate mapping keys."""


def _construct_mapping(loader: DuplicateKeySafeLoader, node: yaml.MappingNode) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=False)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=False)
    return mapping


DuplicateKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


def metadata_string(value: Any) -> str:
    """Return an unambiguous scalar metadata representation, or an empty string."""
    if value is None:
        return ""
    if isinstance(value, (str, int, float, date, datetime)) and not isinstance(value, bool):
        return value.isoformat() if isinstance(value, (date, datetime)) else str(value)
    return ""


def is_valid_version(value: Any) -> bool:
    return bool(VERSION_PATTERN.fullmatch(metadata_string(value)))


def is_valid_iso8601(value: Any) -> bool:
    raw = metadata_string(value)
    if not raw:
        return False
    try:
        datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        try:
            date.fromisoformat(raw)
        except ValueError:
            return False
    return True
