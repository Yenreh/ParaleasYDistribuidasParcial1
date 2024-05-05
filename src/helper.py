import json

from pathlib import Path


def loadJSON(file_path: str):
    if Path(file_path).is_file() is False:
        raise FileNotFoundError(f"File not found: {file_path}")
    return json.loads(readFile(file_path))


def readFile(file_path: str):
    try:
        with Path(file_path).open() as data:
            return data.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
