import json
import requests
import os

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


def downloadFile(url, save_path, file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{save_path}/{file_name}", 'wb') as f:
                f.write(response.content)
            return True
        else:
            print("Failed to download the file. Status code:", response.status_code)
            return False
    except Exception as e:
        print("An error occurred while downloading the file:", e)
        return False