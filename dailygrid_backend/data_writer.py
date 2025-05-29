import json
from pathlib import Path

from dailygrid_backend.config import OUTPUT_FILE


def write_json(data: dict, path: str = OUTPUT_FILE):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
