"""
Knowledge Dictionary - A Python package for storing serializable metadata.

This package provides templates and utilities for working with knowledge dictionaries.
"""

from .templates import KNOWLEDGE_TEMPLATE, MINIMAL_TEMPLATE, EXTENDED_TEMPLATE
from .knowledgedict import KnowledgeDict

__version__ = "0.1.0"
__all__ = [
    "KnowledgeDict",
    "KNOWLEDGE_TEMPLATE",
    "MINIMAL_TEMPLATE",
    "EXTENDED_TEMPLATE",
]
