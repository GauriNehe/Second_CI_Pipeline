import importlib

module = importlib.import_module("codes.32_count_words")

def test_count_words_normal():
    assert module.count_words("Python CI pipeline with GitHub Actions") == 6

def test_count_words_empty():
    assert module.count_words("   ") == 0
