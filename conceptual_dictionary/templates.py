sample_template = {
    "id": "sample1",
    "material": {
        "element_ratio": {},
        "crystal_structure": {
            "spacegroup_symbol": None,
            "spacegroup_number": None,
            "unit_cell": {
                "bravais_lattice": None,
                "lattice_parameter": None,
                "angle": [],
            },
        },
    },
    "simulation_cell": {
        "volume": {"value": None},
        "number_of_atoms": None,
        "length": [],
        "vector": [],
        "angle": [],
        "repetitions": [],
        "grain_size": None,
        "number_of_grains": 0,
    },
    "atom_attribute": {
        "position": None,
        "species": None,
    },
    "calculated_property": [],
}

property_template = {
    "basename": None,
    "value": None,
    "unit": None,
    "associate_to_sample": [],
}

workflow_template = {
    "algorithm": None,
    "method": None,
    "xc_functional": None,
    "input_parameter": [],
    "input_sample": [],
    "output_sample": [],
    "calculated_property": [],
    "degrees_of_freedom": [],
    "interatomic_potential": {
        "potential_type": None,
        "uri": None,
    },
    "software": {
        "uri": None,
        "version": None,
        "label": None,
    },
    "workflow_manager": {
        "uri": None,
        "version": None,
        "label": None,
    },
    "thermodynamic_ensemble": None,
}

# Operation template for atomic-scale transformations
# Contains all possible fields for all operation types
operation_template = {
    "method": None,  # Required: DeleteAtom, SubstituteAtom, AddAtom, Rotate, Translate, Shear
    "input_sample": None,  # Required
    "output_sample": None,  # Required
    # Optional fields (used by specific operations):
    "rotation_matrix": None,  # For Rotate: 3x3 matrix, e.g., [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    "translation_vector": None,  # For Translate: 3D vector, e.g., [1.5, 2.0, 0.5]
    "shear_vector": None,  # For Shear: 3D vector, e.g., [0.1, 0, 0]
    "normal_vector": None,  # For Shear (optional): 3D vector, e.g., [1, 1, 1]
    "distance": None,  # For Shear (optional): float
}
