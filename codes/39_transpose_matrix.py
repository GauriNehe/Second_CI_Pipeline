def transpose_matrix(matrix: list) -> list:
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]