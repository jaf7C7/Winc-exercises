# Do not modify these lines
import os

__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"
__human_name__ = "errors"


# Test your functions here to make sure the functionality remains the same.
def main():
    # 'add()'
    input = [("foo", "bar"), (10, 20), ("foo", 20)]
    for i in input:
        assert add_LBYL(i[0], i[1]) == add(i[0], i[1])
    # 'read_file()'
    with open("foo", "w") as f:
        f.write("This is file 'foo' and I exist")
    files = ["foo", "bar"]
    for f in files:
        assert read_file_LBYL(f) == read_file(f)
    # 'get_item_from_list()'
    my_list = list(range(10))
    indices = [9, -1, 10]
    for i in indices:
        assert get_item_from_list_LBYL(my_list, i) == get_item_from_list(
            my_list, i
        )


"""Change the three functions below from Look Before You Leap (LBYL) to Easier
to Ask for Forgiveness than Permission (EAFP)"""


# Returns the addition of x and y if it's defined, otherwise returns 0
# Look before you leap (LBYL)
def add_LBYL(x, y):
    if type(x) is str and (type(y) is int or type(y) is float):
        return 0
    elif type(y) is str and (type(x) is int or type(x) is float):
        return 0
    return x + y


# Easier to ask for forgiveness than permission (EAFP)
def add(x, y):
    try:
        return x + y
    except TypeError:
        return 0


# Returns the contents of the file at 'filename', or an empty string if the
# file does not exist
def read_file_LBYL(filename):
    if os.path.exists(filename):
        return open(filename, "r").read()
    else:
        return ""


def read_file(filename):
    try:
        return open(filename, "r").read()
    except FileNotFoundError:
        return ""


# Returns item at `index` from list `l` if possible, otherwise returns None
def get_item_from_list_LBYL(l, index):
    max_index = len(l) - 1
    min_index = -1 - max_index
    if index <= max_index and index >= min_index:
        return l[index]
    else:
        return None


def get_item_from_list(l, index):
    try:
        return l[index]
    except IndexError:
        return None


if __name__ == "__main__":
    main()
