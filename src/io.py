import os

cache_dir = "files"

storage_folders = {
        "photo": "photos" + os.sep,
        "document": "documents" + os.sep,
        "text": "data" + os.sep,
        "video": "videos" + os.sep
        }


def create_cache_dir():
    #  Create the data folder
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    return 0
