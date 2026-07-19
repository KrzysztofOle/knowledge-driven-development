"""Small local HTML interface for the KGAID approval MVP."""

from __future__ import annotations

import html
from urllib.parse import quote

from bleach.css_sanitizer import CSSSanitizer
from bleach.sanitizer import Cleaner
from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.tasklists import tasklists_plugin

from .repository import Document

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


def render_markdown(markdown: str) -> str:
    """Render Markdown as allow-list-sanitized HTML for local review."""
    return _MARKDOWN_CLEANER.clean(_MARKDOWN.render(markdown))


def page(title: str, content: str, message: str | None = None, error: str | None = None) -> str:
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
</style></head><body><header><p><a href="/">Kolejka akceptacji</a></p><h1>{html.escape(title)}</h1></header>{notice}{content}</body></html>"""


def queue_page(
    documents: list[Document], message: str | None = None, error: str | None = None
) -> str:
    if not documents:
        content = "<p>Brak dokumentów oczekujących na akceptację.</p>"
    else:
        rows = []
        for document in documents:
            path = document.relative_path.as_posix()
            preview_url = f"/document?path={quote(path)}"
            rows.append(
                "<tr>"
                f"<td>{html.escape(document.document_id or '—')}</td>"
                f"<td>{html.escape(document.title)}</td>"
                f"<td><code>{html.escape(path)}</code></td>"
                f'<td><a href="{preview_url}">Podgląd</a></td>'
                '<td><form method="post" action="/approve">'
                f'<input type="hidden" name="path" value="{html.escape(path)}">'
                '<button type="submit">Akceptuj</button></form></td>'
                "</tr>"
            )
        content = (
            "<table><thead><tr><th>ID</th><th>Tytuł</th><th>Ścieżka</th>"
            "<th>Podgląd</th><th>Akceptacja</th></tr></thead><tbody>"
            + "".join(rows)
            + "</tbody></table>"
        )
    return page("Kolejka akceptacji", content, message, error)


def document_page(document: Document, message: str | None = None, error: str | None = None) -> str:
    path = document.relative_path.as_posix()
    content = (
        f"<p><strong>ID:</strong> {html.escape(document.document_id or 'brak')}<br>"
        f"<strong>Ścieżka:</strong> <code>{html.escape(path)}</code></p>"
        '<form method="post" action="/approve">'
        f'<input type="hidden" name="path" value="{html.escape(path)}">'
        '<button type="submit">Akceptuj</button></form><hr>'
        f'<article class="document">{render_markdown(document.body)}</article>'
    )
    return page(document.title, content, message, error)
