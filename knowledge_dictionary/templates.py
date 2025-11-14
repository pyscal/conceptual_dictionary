"""
Templates for knowledge dictionary metadata.

This module provides template dictionaries for storing serializable metadata.
"""

# Base template for knowledge dictionary
KNOWLEDGE_TEMPLATE = {
    "metadata": {
        "version": "1.0",
        "created": None,
        "updated": None,
        "author": None,
    },
    "content": {
        "title": None,
        "description": None,
        "tags": [],
        "data": {},
    },
    "schema": {
        "type": "knowledge_dictionary",
        "format": "json",
    }
}

# Minimal template
MINIMAL_TEMPLATE = {
    "title": None,
    "description": None,
    "data": {},
}

# Extended template with additional fields
EXTENDED_TEMPLATE = {
    "metadata": {
        "version": "1.0",
        "created": None,
        "updated": None,
        "author": None,
        "license": None,
        "source": None,
    },
    "content": {
        "title": None,
        "description": None,
        "tags": [],
        "categories": [],
        "keywords": [],
        "data": {},
        "references": [],
    },
    "schema": {
        "type": "knowledge_dictionary",
        "format": "json",
        "version": "1.0",
    },
    "provenance": {
        "origin": None,
        "modified_by": [],
        "change_log": [],
    }
}
