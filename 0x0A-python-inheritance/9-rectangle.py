#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        private attributes width and height,
        and validating if they are ints.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area: returns the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """prints Rectangle info with format"""
        return f"[Rectangle] {self.__width}/{self.__height}"
