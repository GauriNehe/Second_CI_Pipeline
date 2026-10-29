import importlib

module = importlib.import_module("codes.33_first_non_repeating")

def test_first_non_repeating_found():
    assert module.first_non_repeating("swiss") == "w"

def test_first_non_repeating_none():
    assert module.first_non_repeating("aabbcc") is None
