import importlib

module = importlib.import_module("codes.37_rotate_string")

def test_rotate_string_basic():
    assert module.rotate_string("abcdef", 2) == "cdefab"

def test_rotate_string_full_cycle():
    assert module.rotate_string("python", 6) == "python"
