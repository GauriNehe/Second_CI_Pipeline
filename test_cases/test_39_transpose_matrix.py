import importlib

module = importlib.import_module("codes.39_transpose_matrix")

def test_transpose_rectangular():
    assert module.transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_transpose_square():
    assert module.transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
