"""Safe reading and narrow updates of Markdown YAML front matter."""

from __future__ import annotations

import os
import re
import stat
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


class ApprovalError(Exception):
    """Raised when a document cannot be safely approved."""


class UniqueKeySafeLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects ambiguous duplicate mapping keys."""


def _construct_mapping(loader: UniqueKeySafeLoader, node: yaml.MappingNode) -> dict[Any, Any]:
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


UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)

FRONT_MATTER_DELIMITER = re.compile(r"^(---|\.\.\.)\r?$")
FIELD_LINE = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_-]*):[^\r\n]*(?P<ending>\r?\n|$)")
MARKDOWN_SUFFIXES = {".md", ".markdown"}


@dataclass(frozen=True)
class FrontMatter:
    """Raw and parsed front matter, with document content kept byte-for-byte."""

    raw: str
    metadata: dict[str, Any]
    body: str
    newline: str


@dataclass(frozen=True)
class Document:
    """A pending approval candidate discovered beneath the documentation root."""

    relative_path: Path
    document_id: str | None
    title: str
    body: str


def _line_ending(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def parse_front_matter(text: str) -> FrontMatter | None:
    """Parse a Markdown front-matter block without changing the source text."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        return None

    end_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if FRONT_MATTER_DELIMITER.fullmatch(line.rstrip("\n")):
            end_index = index
            break
    if end_index is None:
        raise ApprovalError("Front matter YAML nie ma końcowego separatora.")

    raw = "".join(lines[1:end_index])
    try:
        parsed = yaml.load(raw, Loader=UniqueKeySafeLoader)
    except yaml.YAMLError as error:
        raise ApprovalError(f"Nieprawidłowy YAML front matter: {error}") from error
    if not isinstance(parsed, dict):
        raise ApprovalError("Front matter YAML musi być mapą pól.")
    if not all(isinstance(key, str) for key in parsed):
        raise ApprovalError("Nazwy pól YAML front matter muszą być tekstem.")

    return FrontMatter(
        raw=raw,
        metadata=parsed,
        body="".join(lines[end_index + 1 :]),
        newline=_line_ending(text),
    )


def _document_title(metadata: dict[str, Any], body: str, fallback: str) -> str:
    title = metadata.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _replace_or_append_field(raw: str, key: str, value: str, newline: str) -> str:
    replacement = f"{key}: {value}{newline}"
    found = False
    result: list[str] = []
    for line in raw.splitlines(keepends=True):
        match = FIELD_LINE.match(line)
        if match and match.group("key") == key:
            result.append(replacement)
            found = True
        else:
            result.append(line)
    if not found:
        if result and not result[-1].endswith(("\n", "\r")):
            result.append(newline)
        result.append(replacement)
    return "".join(result)


def _yaml_scalar(value: str) -> str:
    """Serialize one string as a YAML scalar without a document end marker."""
    serialized = yaml.safe_dump(
        [value],
        allow_unicode=True,
        default_flow_style=True,
        width=2**31 - 1,
    ).strip()
    if not serialized.startswith("[") or not serialized.endswith("]"):
        raise ApprovalError("Nie można bezpiecznie zserializować wartości YAML.")
    return serialized[1:-1]


def update_front_matter(front_matter: FrontMatter, approver: str, approved_at: str) -> str:
    """Update only approval fields, retaining every other YAML line and body."""
    raw = front_matter.raw
    raw = _replace_or_append_field(raw, "approval_status", "approved", front_matter.newline)
    raw = _replace_or_append_field(
        raw,
        "approved_by",
        _yaml_scalar(approver),
        front_matter.newline,
    )
    raw = _replace_or_append_field(raw, "approved_at", approved_at, front_matter.newline)
    return f"---{front_matter.newline}{raw}---{front_matter.newline}{front_matter.body}"


class DocumentationRepository:
    """A bounded documentation directory that exposes only pending Markdown files."""

    def __init__(self, documentation_dir: str | Path) -> None:
        root = Path(documentation_dir).expanduser()
        if not root.is_dir():
            raise ApprovalError(f"Katalog dokumentacji nie istnieje: {root}")
        self.root = root.resolve()

    def _resolve_document(self, relative_path: str | Path) -> Path:
        candidate = Path(relative_path)
        if candidate.is_absolute() or ".." in candidate.parts:
            raise ApprovalError(
                "Ścieżka dokumentu musi być względna względem katalogu dokumentacji."
            )
        if candidate.suffix.lower() not in MARKDOWN_SUFFIXES:
            raise ApprovalError("Można zatwierdzać wyłącznie pliki Markdown.")
        target = (self.root / candidate).resolve()
        if not target.is_relative_to(self.root) or not target.is_file():
            raise ApprovalError("Wybrany dokument nie znajduje się w katalogu dokumentacji.")
        return target

    def _read_front_matter(self, path: Path) -> FrontMatter:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            raise ApprovalError(f"Nie można odczytać dokumentu: {error}") from error
        front_matter = parse_front_matter(text)
        if front_matter is None:
            raise ApprovalError("Dokument nie zawiera YAML front matter.")
        return front_matter

    def pending_documents(self) -> list[Document]:
        """Return only explicitly pending, valid Markdown documents below ``root``."""
        documents: list[Document] = []
        for path in self.root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in MARKDOWN_SUFFIXES:
                continue
            try:
                resolved = path.resolve()
                if not resolved.is_relative_to(self.root):
                    continue
                front_matter = self._read_front_matter(resolved)
            except ApprovalError:
                continue
            if front_matter.metadata.get("approval_status") != "pending":
                continue
            documents.append(
                Document(
                    relative_path=resolved.relative_to(self.root),
                    document_id=_string_metadata(front_matter.metadata, "document_id", "id"),
                    title=_document_title(front_matter.metadata, front_matter.body, resolved.stem),
                    body=front_matter.body,
                )
            )
        return sorted(documents, key=lambda document: document.relative_path.as_posix())

    def pending_document(self, relative_path: str | Path) -> Document:
        target = self._resolve_document(relative_path)
        front_matter = self._read_front_matter(target)
        if front_matter.metadata.get("approval_status") != "pending":
            raise ApprovalError("Dokument nie oczekuje na akceptację.")
        return Document(
            relative_path=target.relative_to(self.root),
            document_id=_string_metadata(front_matter.metadata, "document_id", "id"),
            title=_document_title(front_matter.metadata, front_matter.body, target.stem),
            body=front_matter.body,
        )

    def approve(self, relative_path: str | Path, approver: str) -> Document:
        """Atomically approve one currently pending document inside the configured root."""
        if not approver.strip():
            raise ApprovalError("Nazwa osoby zatwierdzającej jest wymagana.")
        if "\n" in approver or "\r" in approver:
            raise ApprovalError("Nazwa osoby zatwierdzającej nie może zawierać znaku nowej linii.")
        target = self._resolve_document(relative_path)
        front_matter = self._read_front_matter(target)
        if front_matter.metadata.get("approval_status") != "pending":
            raise ApprovalError("Dokument nie oczekuje na akceptację.")

        approved_at = datetime.now().astimezone().isoformat(timespec="seconds")
        content = update_front_matter(front_matter, approver.strip(), approved_at)
        self._atomic_write(target, content)
        return Document(
            relative_path=target.relative_to(self.root),
            document_id=_string_metadata(front_matter.metadata, "document_id", "id"),
            title=_document_title(front_matter.metadata, front_matter.body, target.stem),
            body=front_matter.body,
        )

    @staticmethod
    def _atomic_write(target: Path, content: str) -> None:
        mode = stat.S_IMODE(target.stat().st_mode)
        descriptor, temporary_name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
        temporary_path = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.chmod(temporary_path, mode)
            os.replace(temporary_path, target)
            directory_descriptor = os.open(target.parent, os.O_RDONLY)
            try:
                os.fsync(directory_descriptor)
            finally:
                os.close(directory_descriptor)
        except OSError as error:
            raise ApprovalError(f"Nie można bezpiecznie zapisać dokumentu: {error}") from error
        finally:
            temporary_path.unlink(missing_ok=True)


def _string_metadata(metadata: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = metadata.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None
