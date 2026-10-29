import importlib

module = importlib.import_module("codes.40_gcd")

def test_gcd_common():
    assert module.find_gcd(48, 18) == 6

def test_gcd_coprime():
    assert module.find_gcd(17, 13) == 1
