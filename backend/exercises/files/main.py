# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

import os
import zipfile


def clean_cache():
    cache_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "cache"
    )
    if os.path.isdir(cache_path):
        for root, dirs, files in os.walk(cache_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    else:
        os.mkdir(cache_path)


def cache_zip(zip_file, dir):
    # Unpack 'zip_file' into 'dir'
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(dir)


def cached_files():
    cache_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "cache"
    )
    cached_files = []
    for root, dirs, files in os.walk(cache_path):
        for file in files:
            cached_files.append(os.path.join(root, file))
    return cached_files


def find_password(files):
    for file in files:
        with open(file, "r") as file:
            for line in file:
                if "password" in line:
                    return line[len("password: "):-1]  # '-1' to omit '\n'


if __name__ == "__main__":
    print(find_password(cached_files()))
