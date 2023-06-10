#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """informal string representation of the square"""
        return f"[Square] {self.__width}/{self.__height}"
