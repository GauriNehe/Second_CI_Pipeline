import importlib

module = importlib.import_module("codes.38_missing_number_xor")

def test_missing_number_middle():
    assert module.find_missing_xor([1, 2, 4, 5, 6]) == 3

def test_missing_number_first():
    assert module.find_missing_xor([2, 3, 4]) == 1
    
