import os


def ensure_download_directory(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)
