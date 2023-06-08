def matrix_divided(matrix, div):
    if isinstance(matrix, list):
        if all(isinstance(row, list) and all(isinstance(n, int) for n in row) for row in matrix):
            pass
