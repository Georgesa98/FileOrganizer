import json
import os
from pathlib import Path


def organize(*args, dir):
    ext_dir = Path(__file__).parent
    file_path = ext_dir / "file_extensions.json"
    with open(file_path, "r") as file:
        extensions = json.load(fp=file)
    files = os.listdir(dir)
    for file in files:
        for key, values in extensions.items():
            for value in values:
                if file.endswith(value):
                    filtered_dir = Path(os.path.join(dir, key))
                    if not filtered_dir.exists():
                        Path.mkdir(filtered_dir, exist_ok=True, parents=True)
                    break
