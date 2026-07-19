"""Small local HTML interface for the KGAID approval MVP."""

from __future__ import annotations

import html
import re
from urllib.parse import quote

from .repository import Document


def render_markdown(markdown: str) -> str:
    """Render a deliberately small, safe Markdown subset for local review."""
    output: list[str] = []
    paragraph: list[str] = []
    in_code = False
    list_open = False

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{_inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        if line.startswith("```"):
            flush_paragraph()
            if list_open:
                output.append("</ul>")
                list_open = False
            output.append("<pre><code>" if not in_code else "</code></pre>")
            in_code = not in_code
            continue
        if in_code:
            output.append(html.escape(f"{raw_line}\n"))
            continue
        if not line:
            flush_paragraph()
            if list_open:
                output.append("</ul>")
                list_open = False
            continue
        heading = re.fullmatch(r"(#{1,6})\s+(.+)", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            output.append(f"<h{level}>{_inline(heading.group(2))}</h{level}>")
            continue
        if line.startswith(("- ", "* ")):
            flush_paragraph()
            if not list_open:
                output.append("<ul>")
                list_open = True
            output.append(f"<li>{_inline(line[2:])}</li>")
            continue
        if list_open:
            output.append("</ul>")
            list_open = False
        paragraph.append(line)
    flush_paragraph()
    if list_open:
        output.append("</ul>")
    if in_code:
        output.append("</code></pre>")
    return "\n".join(output)


def _inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return re.sub(r"\[([^]]+)\]\(([^ )]+)\)", r'<a href="\2">\1</a>', escaped)


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
.document {{ border: 1px solid #d9e0e6; padding: 1.5rem; border-radius: .25rem; }} pre {{ background: #f1f3f5; padding: 1rem; overflow-x: auto; }} code {{ background: #f1f3f5; padding: .1rem .25rem; }}
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
