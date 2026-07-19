"""Command-line entry point for the local KGAID approval interface."""

from __future__ import annotations

import argparse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse

from .repository import ApprovalError, DocumentationRepository
from .web import document_page, page, queue_page


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Lokalna kolejka akceptacji dokumentacji KGAID.")
    parser.add_argument(
        "--docs-dir", type=Path, required=True, help="Katalog dokumentacji do przeglądu."
    )
    parser.add_argument("--approver", required=True, help="Imię i nazwisko osoby zatwierdzającej.")
    parser.add_argument(
        "--host", default="127.0.0.1", help="Adres lokalnego interfejsu (domyślnie 127.0.0.1)."
    )
    parser.add_argument(
        "--port", type=int, default=8765, help="Port lokalnego interfejsu (domyślnie 8765)."
    )
    return parser


def make_handler(
    repository: DocumentationRepository, approver: str
) -> type[BaseHTTPRequestHandler]:
    class ApprovalHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            request = urlparse(self.path)
            parameters = parse_qs(request.query)
            if request.path == "/":
                self._send_html(
                    queue_page(
                        repository.pending_documents(),
                        _first(parameters, "message"),
                        _first(parameters, "error"),
                    )
                )
                return
            if request.path == "/document":
                try:
                    document = repository.pending_document(_required(parameters, "path"))
                    self._send_html(document_page(document))
                except ApprovalError as error:
                    self._send_html(
                        page("Błąd", "<p>Nie można wyświetlić dokumentu.</p>", error=str(error)),
                        HTTPStatus.BAD_REQUEST,
                    )
                return
            self._send_html(
                page("Nie znaleziono", "<p>Nie ma takiego widoku.</p>"), HTTPStatus.NOT_FOUND
            )

        def do_POST(self) -> None:  # noqa: N802
            if urlparse(self.path).path != "/approve":
                self._send_html(
                    page("Nie znaleziono", "<p>Nie ma takiej akcji.</p>"), HTTPStatus.NOT_FOUND
                )
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                payload = parse_qs(self.rfile.read(length).decode("utf-8"))
                document = repository.approve(_required(payload, "path"), approver)
                self.send_response(HTTPStatus.SEE_OTHER)
                self.send_header(
                    "Location",
                    f"/?message={quote(f'Zaakceptowano {document.relative_path.as_posix()}', safe='')}",
                )
                self.end_headers()
            except (ApprovalError, UnicodeDecodeError, ValueError) as error:
                self._send_html(
                    page("Błąd", "<p>Dokument nie został zmieniony.</p>", error=str(error)),
                    HTTPStatus.BAD_REQUEST,
                )

        def _send_html(self, content: str, status: HTTPStatus = HTTPStatus.OK) -> None:
            encoded = content.encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

        def log_message(self, _format: str, *_args: object) -> None:
            return

    return ApprovalHandler


def _first(values: dict[str, list[str]], name: str) -> str | None:
    return values.get(name, [None])[0]


def _required(values: dict[str, list[str]], name: str) -> str:
    value = _first(values, name)
    if not value:
        raise ApprovalError(f"Brak wymaganego parametru: {name}.")
    return value


def main() -> None:
    args = build_parser().parse_args()
    try:
        repository = DocumentationRepository(args.docs_dir)
    except ApprovalError as error:
        raise SystemExit(f"Błąd konfiguracji: {error}") from error
    server = ThreadingHTTPServer((args.host, args.port), make_handler(repository, args.approver))
    print(f"KGAID Documentation Approval: http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nZatrzymano serwer.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
