#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.
    Args:
        size (int): The height/width of the square.
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
