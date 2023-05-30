class Square:
    def __init__(self, size=0):
        """Initializes a Square instance.
        Args:
            size (int): The size of the square (default is 0).
        Returns:
            None        
        """
        self.size = size

    def area(self):
        """Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the __size attribute.
        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the __size attribute.
        Args:
            value (int): The size value to be set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
