# conceptual_dictionary

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
from conceptual_dictionary.templates import sample_template, property_template, workflow_template

# Use a template directly
my_data = sample_template.copy()
my_data['material']['element_ratio'] = {'Fe': 0.7, 'C': 0.3}
my_data['simulation_cell']['volume']['value'] = 1000
```

### Using ConceptualDict Class

Work with conceptual dictionaries using the ConceptualDict class:

```python
from conceptual_dictionary.conceptualdict import ConceptualDict

# Create a new conceptual dictionary
cd = ConceptualDict()

# Set values using dot notation
cd.set("material.element_ratio.Fe", 0.7)
cd.set("material.element_ratio.C", 0.3)
cd.set("simulation_cell.volume.value", 1000)

# Get values
fe_ratio = cd.get("material.element_ratio.Fe")
volume = cd.get("simulation_cell.volume.value")

# Convert to standard dictionary
data = cd.to_dict()

# Serialize to JSON
json_str = cd.to_json(indent=2)

# Save to file
cd.save("my_conceptual.json")

# Load from file
cd_loaded = ConceptualDict.from_json("my_conceptual.json")
```

## Available Templates

- **sample_template**: Standard template with metadata, content, and schema sections
- **property_template**: Template for defining properties with values and units
- **workflow_template**: Template for describing workflows, including algorithms and methods

## License

MIT License
