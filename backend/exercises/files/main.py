# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line


import os


def clean_cache():
    cache_path = "cache"
    # Create dir 'cache' in cwd if it doesn't exist already
    if not os.path.isdir(cache_path):
        os.mkdir(cache_path)
    # If the cache is not empty recursively delete all files and subdirs, but
    # leave the cache dir itself
    #
    # TODO: Check if this deletes all files in all subdirs recursively
    #
    for dir_name, sub_dirs, files in os.walk("cache"):
        for file in files:
            os.remove(os.path.join(dir_name, file))
        if dir_name != cache_path:
            os.rmdir(dir_name)

clean_cache()
