#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.appen(new_row)
    return new_matrix
