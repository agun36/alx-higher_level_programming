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

    @property
    def size(self):
        """Retrieve the si
        ze of the square.
        """
        return self.__size

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
    def __eq__(self, other):
        """Check if two squares are equal based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the squares have equal areas, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the squares have different areas, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if d square is smaller than d other square based on their are

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the square is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if d squ is smaller or == to d other square based on their ar

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the square is smaller or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the square is > than d other square based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the square is greater or equal to the other square based

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the square is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
