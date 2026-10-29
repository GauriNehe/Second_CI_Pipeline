import importlib

module = importlib.import_module("codes.34_check_sorted")

def test_is_sorted_true():
    assert module.is_sorted([1, 2, 2, 4, 5]) is True

def test_is_sorted_false():
    assert module.is_sorted([1, 5, 3, 4]) is False
