import os
import json


def rename_files(directory_path: str, collected_information_file_path: str) -> None:
    information = []
    with open(collected_information_file_path, "r") as f:
        for line in f.readlines():
            information.append(json.loads(line.split(" \n")[0]))
    for file_info in information:
        filename = file_info['downloaded_file_name']
        new_file_name = file_info['file_name']
        if filename in os.listdir(directory_path):
            old_path = os.path.join(directory_path, filename)
            new_path = os.path.join(directory_path, new_file_name)
            os.rename(old_path, new_path)

