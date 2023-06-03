#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides elements of a matrix by a number.

    Args:
        matrix (list): List of lists of ints or floats.
        div (int/float): Number to divide matrix elements.

    Returns:
        list: New matrix with elements divided by number.

    Raises:
        TypeError: If matrix is not a matrix of ints/floats.
        ZeroDivisionError: If div is zero.

    """

    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
