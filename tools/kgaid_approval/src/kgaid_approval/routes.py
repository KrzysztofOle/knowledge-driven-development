"""Named routes and request parameters for the approval web application."""

from __future__ import annotations

from enum import StrEnum


class Endpoint(StrEnum):
    """Flask endpoint names used to construct internal URLs."""

    QUEUE = "queue"
    DOCUMENT = "document"
    APPROVE = "approve"


QUEUE_ROUTE = "/"
DOCUMENT_ROUTE = "/document"
APPROVE_ROUTE = "/approve"

PATH_PARAMETER = "path"
MESSAGE_PARAMETER = "message"
ERROR_PARAMETER = "error"
