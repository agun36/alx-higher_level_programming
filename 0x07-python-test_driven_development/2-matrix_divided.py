#!/usr/bin/python3
#!/usr/bin/python3
"""
Module containing matrix_divided function.

"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): List of lists containing integers or floats.
        div (int or float): Divisor.

    Returns:
        list: New matrix with elements divided by the divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
            or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
