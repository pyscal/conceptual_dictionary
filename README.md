# knowledge_dictionary

A Python dictionary template for storing serializable metadata.

## Installation

Install from source:

```bash
pip install -e .
```

## Usage

### Using Templates

Import and use predefined dictionary templates:

```python
from knowledge_dictionary import KNOWLEDGE_TEMPLATE, MINIMAL_TEMPLATE, EXTENDED_TEMPLATE

# Use a template directly
my_data = KNOWLEDGE_TEMPLATE.copy()
my_data['metadata']['author'] = 'John Doe'
my_data['content']['title'] = 'My Knowledge'
```

### Using KnowledgeDict Class

Work with knowledge dictionaries using the KnowledgeDict class:

```python
from knowledge_dictionary import KnowledgeDict

# Create a new knowledge dictionary
kd = KnowledgeDict(template="knowledge")

# Set values using dot notation
kd.set("metadata.author", "John Doe")
kd.set("content.title", "My Knowledge")
kd.set("content.description", "A collection of important information")

# Get values
author = kd.get("metadata.author")
title = kd.get("content.title")

# Convert to standard dictionary
data = kd.to_dict()

# Serialize to JSON
json_str = kd.to_json(indent=2)

# Save to file
kd.save("my_knowledge.json")

# Load from file
kd_loaded = KnowledgeDict.load("my_knowledge.json")
```

## Available Templates

- **KNOWLEDGE_TEMPLATE**: Standard template with metadata, content, and schema sections
- **MINIMAL_TEMPLATE**: Minimal template with just title, description, and data
- **EXTENDED_TEMPLATE**: Extended template with additional provenance tracking

## License

MIT License
