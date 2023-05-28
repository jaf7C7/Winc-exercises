# Create a sample directory tree

import os
import sys


# Make a single directory containing 3 files in a target dir
def populate(dir):
    if os.path.isfile(dir):
        return "No"  # TODO: Proper error handling
    if not os.path.isdir(dir):
        os.mkdir(dir)
    for i in range(3):
        file = os.path.join(dir, f"file_{i}")
        with open(file, "x"):
            pass


# Recursively call populate to the given depth
def mktree(dir, depth=3):
    if depth < 1:
        return
    populate(dir)
    depth -= 1
    for i in range(3):
        sub_dir = os.path.join(dir, f"dir_{i}")
        mktree(sub_dir, depth)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments given")
    else:
        mktree(sys.argv[1])
