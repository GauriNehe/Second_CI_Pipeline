import importlib

module = importlib.import_module("codes.36_most_frequent")

def test_most_frequent_element():
    assert module.most_frequent([1, 3, 2, 1, 4, 1, 3]) == 1

def test_most_frequent_strings():
    assert module.most_frequent(["a", "b", "b", "c"]) == "b"
