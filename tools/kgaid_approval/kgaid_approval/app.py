"""Flask application factory for the KGAID approval interface."""

from __future__ import annotations

from http import HTTPStatus

from flask import Flask, redirect, request, url_for

from .repository import ApprovalError, DocumentationRepository
from .routes import (
    APPROVE_ROUTE,
    DOCUMENT_ROUTE,
    ERROR_PARAMETER,
    MESSAGE_PARAMETER,
    PATH_PARAMETER,
    QUEUE_ROUTE,
    Endpoint,
)
from .web import document_page, page, queue_page


def create_app(repository: DocumentationRepository, approver: str) -> Flask:
    """Create the local approval application bound to one repository and approver."""
    app = Flask(__name__)

    @app.get(QUEUE_ROUTE, endpoint=Endpoint.QUEUE)
    def queue() -> str:
        documents = repository.pending_documents()
        preview_urls = {
            document.relative_path: url_for(
                Endpoint.DOCUMENT, **{PATH_PARAMETER: document.relative_path.as_posix()}
            )
            for document in documents
        }
        return queue_page(
            documents,
            queue_url=url_for(Endpoint.QUEUE),
            preview_urls=preview_urls,
            approve_url=url_for(Endpoint.APPROVE),
            message=request.args.get(MESSAGE_PARAMETER),
            error=request.args.get(ERROR_PARAMETER),
        )

    @app.get(DOCUMENT_ROUTE, endpoint=Endpoint.DOCUMENT)
    def document() -> tuple[str, int] | str:
        try:
            selected_document = repository.document(_required_request_parameter(PATH_PARAMETER))
        except ApprovalError as error:
            return _error_page(error, HTTPStatus.NOT_FOUND, title="Nie znaleziono")
        return document_page(
            selected_document,
            queue_url=url_for(Endpoint.QUEUE),
            approve_url=url_for(Endpoint.APPROVE),
            documentation_dir=repository.root,
            document_url=lambda path: url_for(Endpoint.DOCUMENT, **{PATH_PARAMETER: path}),
        )

    @app.post(APPROVE_ROUTE, endpoint=Endpoint.APPROVE)
    def approve() -> tuple[str, int] | str:
        try:
            approved_document = repository.approve(
                _required_request_parameter(PATH_PARAMETER), approver
            )
        except ApprovalError as error:
            return _error_page(error, HTTPStatus.BAD_REQUEST)
        return redirect(
            url_for(
                Endpoint.QUEUE,
                **{
                    MESSAGE_PARAMETER: (
                        f"Zaakceptowano {approved_document.relative_path.as_posix()}"
                    )
                },
            ),
            code=HTTPStatus.SEE_OTHER,
        )

    return app


def _required_request_parameter(name: str) -> str:
    value = request.values.get(name)
    if not value:
        raise ApprovalError(f"Brak wymaganego parametru: {name}.")
    return value


def _error_page(
    error: ApprovalError, status: HTTPStatus, *, title: str = "Błąd"
) -> tuple[str, int]:
    return (
        page(
            title,
            "<p>Dokument nie został zmieniony.</p>",
            queue_url=url_for(Endpoint.QUEUE),
            error=str(error),
        ),
        status,
    )
