def get_none():
    return None


def flatten_list(l):
    flat_list = []
    for i in l:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list


def flatten_dict(d):
    flat_dict = []
    for i in d.values():
        if isinstance(i, dict):
            flat_dict.extend(flatten_dict(i))
        else:
            flat_dict.append(i)
    return flat_dict


def flatten(x):
    flat_x = []
    if isinstance(x, list):
        for i in x:
            flat_x.extend(flatten(i))
    elif isinstance(x, dict):
        for i in x.values():
            flat_x.extend(flatten(i))
    else:
        flat_x.append(x)
    return flat_x


if __name__ == "__main__":
    print(flatten_list(["a", ["b", ["c", "d"]], "e"]))
    print(
        flatten_dict(
            {
                "a": {
                    "inner_a": 42,
                    "inner_b": {"innermost_a": 350, "innermost_b": 10},
                },
                "b": 3.14,
            }
        )
    )
    print(
        flatten(
            {
                "a": [
                    42,
                    [350, {"inner_a": "Hello", "inner_b": 10000}, "foo"],
                ],
                "b": [[3.14, "bar"], "baz"],
            }
        )
    )
