"""Small local HTML interface for the KGAID approval MVP."""

from __future__ import annotations

import html
from collections.abc import Callable
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bleach.css_sanitizer import CSSSanitizer
from bleach.sanitizer import Cleaner
from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.tasklists import tasklists_plugin

from .repository import Document
from .routes import PATH_PARAMETER

_MARKDOWN = (
    MarkdownIt("gfm-like", {"html": False}).use(tasklists_plugin).use(anchors_plugin, max_level=6)
)
_MARKDOWN_CLEANER = Cleaner(
    tags={
        "a",
        "blockquote",
        "br",
        "code",
        "del",
        "em",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "hr",
        "input",
        "li",
        "ol",
        "p",
        "pre",
        "s",
        "strong",
        "table",
        "tbody",
        "td",
        "th",
        "thead",
        "tr",
        "ul",
    },
    attributes={
        "a": {"href", "title"},
        "code": {"class"},
        "h1": {"id"},
        "h2": {"id"},
        "h3": {"id"},
        "h4": {"id"},
        "h5": {"id"},
        "h6": {"id"},
        "input": {"checked", "class", "disabled", "type"},
        "li": {"class"},
        "ol": {"start"},
        "td": {"style"},
        "th": {"style"},
        "ul": {"class"},
    },
    protocols={"http", "https", "mailto"},
    css_sanitizer=CSSSanitizer(allowed_css_properties={"text-align"}),
    strip=True,
    strip_comments=True,
)


def resolve_document_href(
    current_document: Path,
    href: str,
    documentation_dir: Path,
    document_url: Callable[[str], str],
) -> str:
    """Resolve one local Markdown link without allowing it outside ``documentation_dir``."""
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or parsed.query or not parsed.path or href.startswith("#"):
        return href

    decoded_path = parsed.path
    for _ in range(3):
        decoded = unquote(decoded_path)
        if decoded == decoded_path:
            break
        decoded_path = decoded

    if "\\" in decoded_path:
        return href
    link_path = Path(decoded_path)
    if link_path.is_absolute() or link_path.suffix.lower() not in {".md", ".markdown"}:
        return href

    root = documentation_dir.resolve()
    parts = link_path.parts
    if parts and parts[0] == root.name:
        candidate = root.joinpath(*parts[1:])
    else:
        candidate = root / current_document.parent / link_path
    resolved = candidate.resolve()
    if not resolved.is_relative_to(root):
        return href

    target_url = document_url(resolved.relative_to(root).as_posix())
    if parsed.fragment:
        target_url = f"{target_url}#{parsed.fragment}"
    return target_url


def render_markdown(
    markdown: str,
    *,
    current_document: Path | None = None,
    documentation_dir: Path | None = None,
    document_url: Callable[[str], str] | None = None,
) -> str:
    """Render Markdown as allow-list-sanitized HTML for local review."""
    tokens = _MARKDOWN.parse(markdown)
    if current_document is not None and documentation_dir is not None and document_url is not None:
        for token in tokens:
            for child in token.children or ():
                if child.type == "link_open":
                    href = child.attrGet("href")
                    if href is not None:
                        child.attrSet(
                            "href",
                            resolve_document_href(
                                current_document, href, documentation_dir, document_url
                            ),
                        )
    rendered = _MARKDOWN.renderer.render(tokens, _MARKDOWN.options, {})
    return _MARKDOWN_CLEANER.clean(rendered)


def page(
    title: str,
    content: str,
    *,
    queue_url: str,
    message: str | None = None,
    error: str | None = None,
) -> str:
    notice = ""
    if message:
        notice = f'<p class="notice success">{html.escape(message)}</p>'
    if error:
        notice = f'<p class="notice error">{html.escape(error)}</p>'
    return f"""<!doctype html>
<html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — KGAID Documentation Approval</title>
<style>
body {{ font-family: system-ui, sans-serif; line-height: 1.5; max-width: 980px; margin: 2rem auto; padding: 0 1rem; color: #17202a; }}
a {{ color: #0757a5; }} table {{ width: 100%; border-collapse: collapse; }} th, td {{ padding: .7rem; border-bottom: 1px solid #d9e0e6; text-align: left; vertical-align: top; }}
button {{ background: #087f5b; color: white; border: 0; border-radius: .25rem; padding: .55rem .8rem; font: inherit; cursor: pointer; }}
.notice {{ padding: .8rem 1rem; border-radius: .25rem; }} .success {{ background: #d3f9d8; }} .error {{ background: #ffe3e3; }}
.document {{ border: 1px solid #d9e0e6; padding: 1.5rem; border-radius: .25rem; overflow-x: auto; }}
.document table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
.document th, .document td {{ padding: .6rem .8rem; border: 1px solid #d0d7de; text-align: left; vertical-align: top; }}
.document th {{ background: #f6f8fa; font-weight: 600; }}
.document tbody tr:nth-child(even) {{ background: #f6f8fa; }}
.document tbody tr:hover {{ background: #eef3f8; }}
.document pre {{ background: #f6f8fa; border-radius: .375rem; padding: 1rem; overflow-x: auto; }}
.document code {{ background: #f1f3f5; border-radius: .25rem; padding: .1rem .3rem; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; }}
.document pre code {{ background: transparent; border-radius: 0; padding: 0; }}
.document blockquote {{ margin-left: 0; padding-left: 1rem; border-left: .25rem solid #d0d7de; color: #57606a; }}
.document .task-list-item {{ list-style: none; }}
.document .task-list-item input {{ margin: 0 .4rem 0 -1.4rem; }}
code {{ background: #f1f3f5; padding: .1rem .25rem; }}
</style></head><body><header><p><a href="{html.escape(queue_url, quote=True)}">Kolejka akceptacji</a></p><h1>{html.escape(title)}</h1></header>{notice}{content}</body></html>"""


def queue_page(
    documents: list[Document],
    *,
    queue_url: str,
    preview_urls: dict[Path, str],
    approve_url: str,
    message: str | None = None,
    error: str | None = None,
) -> str:
    if not documents:
        content = "<p>Brak dokumentów oczekujących na akceptację.</p>"
    else:
        rows = []
        for document in documents:
            path = document.relative_path.as_posix()
            preview_url = preview_urls[document.relative_path]
            rows.append(
                "<tr>"
                f"<td>{html.escape(document.document_id or '—')}</td>"
                f"<td>{html.escape(document.title)}</td>"
                f"<td><code>{html.escape(path)}</code></td>"
                f'<td><a href="{html.escape(preview_url, quote=True)}">Podgląd</a></td>'
                f'<td><form method="post" action="{html.escape(approve_url, quote=True)}">'
                f'<input type="hidden" name="{PATH_PARAMETER}" value="{html.escape(path)}">'
                '<button type="submit">Akceptuj</button></form></td>'
                "</tr>"
            )
        content = (
            "<table><thead><tr><th>ID</th><th>Tytuł</th><th>Ścieżka</th>"
            "<th>Podgląd</th><th>Akceptacja</th></tr></thead><tbody>"
            + "".join(rows)
            + "</tbody></table>"
        )
    return page("Kolejka akceptacji", content, queue_url=queue_url, message=message, error=error)


def document_page(
    document: Document,
    *,
    queue_url: str,
    approve_url: str,
    documentation_dir: Path,
    document_url: Callable[[str], str],
    message: str | None = None,
    error: str | None = None,
) -> str:
    path = document.relative_path.as_posix()
    approval_form = ""
    if document.approval_status == "pending":
        approval_form = (
            f'<form method="post" action="{html.escape(approve_url, quote=True)}">'
            f'<input type="hidden" name="{PATH_PARAMETER}" value="{html.escape(path)}">'
            '<button type="submit">Akceptuj</button></form>'
        )
    rendered_document = render_markdown(
        document.body,
        current_document=document.relative_path,
        documentation_dir=documentation_dir,
        document_url=document_url,
    )
    content = (
        f"<p><strong>ID:</strong> {html.escape(document.document_id or 'brak')}<br>"
        f"<strong>Ścieżka:</strong> <code>{html.escape(path)}</code></p>"
        f"{approval_form}<hr>"
        f'<article class="document">{rendered_document}</article>'
    )
    return page(document.title, content, queue_url=queue_url, message=message, error=error)
