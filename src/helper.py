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


def deleteFile(file_path: str):
    try:
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def downloadFile(url, save_path, file_name=None):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if file_name is None:
                with open(f"{save_path}", 'wb') as f:
                    f.write(response.content)
                return True
            else:
                with open(f"{save_path}/{file_name}", 'wb') as f:
                    f.write(response.content)
                return True
        else:
            print("Failed to download the file. Status code:", response.status_code)
            return False
    except Exception as e:
        print("An error occurred while downloading the file:", e)
        return False


def saveLog(log_message, file_path):
    try:
        with open(file_path, 'a') as f:
            f.write(log_message + "\n")
    except Exception as e:
        print("An error occurred while saving the log:", e)


def downloadMP4Video(url, video_output, yt_dl_path):
    command = f'{yt_dl_path} -f mp4 {url} -o "{video_output}"'
    exit_code = os.system(command)
    if exit_code == 0:
        print("Download successful!")
    else:
        print("Download failed.")


def convertToMP3(input_file, output_file):
    command = f'ffmpeg -i "{input_file}" -vn "{output_file}"'
    try:
        os.system(command)
        deleteFile(input_file)
    except Exception as e:
        deleteFile(input_file)
        print("Error:", e)