#!/usr/bin/python3
"""define a class of square """


class Square():
    """initializing private using __size
    Attributes:
        __size (int): __size of the quare
    """
    def __init__(self, size=0):
        """assigning values to private attribute
        Args:
             size (int): size of a quare
        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            
    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            
    def area(self):
        """Find area of square
        Returns:The are of square
        """
        return (self.__size) ** 2
