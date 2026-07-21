"""Local, repository-independent KGAID documentation approval MVP."""

from .app import create_app
from .repository import ApprovalError, Document, DocumentationRepository

__all__ = ["ApprovalError", "Document", "DocumentationRepository", "create_app"]
