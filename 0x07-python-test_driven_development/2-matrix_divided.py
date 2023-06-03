#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): divisor
    Returns:
        A new matrix representing the result of the division.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if not matrix:
        raise TypeError(message)

    if not isinstance(matrix, list):
        raise TypeError(message)

    _matrix = []

    for row in matrix:
        if len(row) == 0 or not isinstance(row, list):
            raise TypeError(message)

        if len(row) != len(matrix[0]):
            raise TypeError(
                    "Each row of the matrix must have the same size"
                    )

        _row = []

        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(message)
            if div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                results = col / div
                _row.append(round(results, 2))

        _matrix.append(_row)

    return _matrix
