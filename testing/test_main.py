from main import *


def test_get_none():
    assert get_none() == None


def test_flatten_dict():
    assert flatten_dict({"a": 42, "b": 3.14}) == [42, 3.14]
    assert flatten_dict({"a": [42, 350], "b": 3.14}) == [[42, 350], 3.14]


def test_recurse_flatten_dict():
    assert recurse_flatten_dict({"a": [42, 350], "b": 3.14}) == [42, 350, 3.14]
    assert recurse_flatten_dict(
        {"a": [42, [350, "foo"]], "b": [[3.14, "bar"], "baz"]}
    ) == [42, 350, "foo", 3.14, "bar", "baz"]
