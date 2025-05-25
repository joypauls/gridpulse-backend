import json
from pathlib import Path


def write_json(data: dict, path: str = "data/us-latest.json"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
