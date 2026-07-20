"""Read-only project health reporting for KGAID documentation."""

from .analysis import ReviewError, analyse_documentation

__all__ = ["ReviewError", "analyse_documentation"]
__version__ = "0.1.0"
