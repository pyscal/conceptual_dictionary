"""
KnowledgeDict class for serializing knowledge dictionary data.

This module provides a class to work with knowledge dictionaries and serialize them
to various formats.
"""

import json
import copy
from datetime import datetime
from typing import Any, Dict, Optional, Union
from pathlib import Path

from .templates import KNOWLEDGE_TEMPLATE, MINIMAL_TEMPLATE, EXTENDED_TEMPLATE


class KnowledgeDict:
    """
    A class for managing and serializing knowledge dictionary data.
    
    This class provides methods to create, manipulate, and serialize
    knowledge dictionaries based on predefined templates.
    """
    
    def __init__(self, template: str = "knowledge", data: Optional[Dict[str, Any]] = None):
        """
        Initialize a KnowledgeDict instance.
        
        Args:
            template: Template type to use ('knowledge', 'minimal', or 'extended')
            data: Optional initial data to populate the dictionary
        """
        self.template_type = template
        self._data = self._get_template(template)
        
        if data:
            self.update(data)
    
    def _get_template(self, template: str) -> Dict[str, Any]:
        """Get a copy of the specified template."""
        templates = {
            "knowledge": KNOWLEDGE_TEMPLATE,
            "minimal": MINIMAL_TEMPLATE,
            "extended": EXTENDED_TEMPLATE,
        }
        
        if template not in templates:
            raise ValueError(f"Unknown template: {template}. Choose from {list(templates.keys())}")
        
        return copy.deepcopy(templates[template])
    
    def update(self, data: Dict[str, Any]) -> None:
        """
        Update the knowledge dictionary with new data.
        
        Args:
            data: Dictionary containing data to update
        """
        self._deep_update(self._data, data)
    
    def _deep_update(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        """Recursively update nested dictionaries."""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._deep_update(target[key], value)
            else:
                target[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a value from the knowledge dictionary.
        
        Args:
            key: Key to retrieve (supports dot notation for nested keys)
            default: Default value if key is not found
            
        Returns:
            Value associated with the key or default
        """
        keys = key.split('.')
        value = self._data
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a value in the knowledge dictionary.
        
        Args:
            key: Key to set (supports dot notation for nested keys)
            value: Value to set
        """
        keys = key.split('.')
        target = self._data
        
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        
        target[keys[-1]] = value
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the KnowledgeDict to a standard dictionary.
        
        Returns:
            Dictionary representation of the knowledge dictionary
        """
        return copy.deepcopy(self._data)
    
    def to_json(self, indent: Optional[int] = 2) -> str:
        """
        Serialize the knowledge dictionary to JSON string.
        
        Args:
            indent: Number of spaces for indentation (None for compact)
            
        Returns:
            JSON string representation
        """
        return json.dumps(self._data, indent=indent, default=str)
    
    def save(self, filepath: Union[str, Path], format: str = "json", indent: Optional[int] = 2) -> None:
        """
        Save the knowledge dictionary to a file.
        
        Args:
            filepath: Path to save the file
            format: Format to save ('json' is currently supported)
            indent: Number of spaces for indentation (for JSON)
        """
        filepath = Path(filepath)
        
        if format == "json":
            with filepath.open('w', encoding='utf-8') as f:
                json.dump(self._data, f, indent=indent, default=str)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    @classmethod
    def load(cls, filepath: Union[str, Path], format: str = "json") -> "KnowledgeDict":
        """
        Load a knowledge dictionary from a file.
        
        Args:
            filepath: Path to the file to load
            format: Format of the file ('json' is currently supported)
            
        Returns:
            KnowledgeDict instance with loaded data
        """
        filepath = Path(filepath)
        
        if format == "json":
            with filepath.open('r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        # Determine template type from loaded data
        template_type = "minimal"
        if "metadata" in data and "schema" in data:
            if "provenance" in data:
                template_type = "extended"
            else:
                template_type = "knowledge"
        
        return cls(template=template_type, data=data)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], template: str = "knowledge") -> "KnowledgeDict":
        """
        Create a KnowledgeDict from a dictionary.
        
        Args:
            data: Dictionary to convert
            template: Template type to use
            
        Returns:
            KnowledgeDict instance
        """
        return cls(template=template, data=data)
    
    def __repr__(self) -> str:
        """String representation of the KnowledgeDict."""
        return f"KnowledgeDict(template='{self.template_type}')"
    
    def __str__(self) -> str:
        """String representation showing the data."""
        return self.to_json(indent=2)
    
    def __getitem__(self, key: str) -> Any:
        """Allow dictionary-style access."""
        return self.get(key)
    
    def __setitem__(self, key: str, value: Any) -> None:
        """Allow dictionary-style setting."""
        self.set(key, value)
