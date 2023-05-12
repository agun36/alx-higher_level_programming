#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Parameters:
    matrix (list): A list of lists of integers

    Format:
    1 2 3
    4 5 6
    7 8 9
    """

    for row in matrix:
        for value in row:
            print("{:d} ".format(value), end="")
        print()
