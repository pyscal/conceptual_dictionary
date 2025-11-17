import yaml
import json
from typing import Any, Dict
import numpy as np
import string
import random

class KnowledgeDict(dict):
    def __init__(self, *args, **kwargs):
        data = {'computational_sample': [], 'workflow': []}
        super().__init__(data, *args, **kwargs)

    def generate_id(self, length=7):
        """Generate a random alphanumeric ID of given length."""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
        
    @staticmethod
    def _clean_data(obj: Any) -> Any:
        if isinstance(obj, dict):
            return {k: KnowledgeDict._clean_data(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [KnowledgeDict._clean_data(v) for v in obj]
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (np.floating, np.float32, np.float64)):
            return float(obj)
        elif isinstance(obj, (np.integer, np.int32, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.bool_, bool)):
            return bool(obj)
        elif obj is None or isinstance(obj, (str, float, int)):
            return obj
        else:
            return str(obj)

    # --------------------
    # YAML I/O
    # --------------------
    def to_yaml(self, filepath: str, sort_keys: bool = False) -> None:
        clean_dict = KnowledgeDict._clean_data(dict(self))
        with open(filepath, 'w') as f:
            yaml.safe_dump(clean_dict, f, sort_keys=sort_keys, allow_unicode=True)

    @classmethod
    def from_yaml(cls, filepath: str) -> "KnowledgeDict":
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        kg = cls()
        kg.update(data)
        return kg

    # --------------------
    # JSON I/O
    # --------------------
    def to_json(self, filepath: str, sort_keys: bool = False, indent: int = 2) -> None:
        clean_dict = KnowledgeDict._clean_data(dict(self))
        with open(filepath, 'w') as f:
            json.dump(clean_dict, f, sort_keys=sort_keys, indent=indent, ensure_ascii=False)

    @classmethod
    def from_json(cls, filepath: str) -> "KnowledgeDict":
        with open(filepath, 'r') as f:
            data = json.load(f)
        kg = cls()
        kg.update(data)
        return kg