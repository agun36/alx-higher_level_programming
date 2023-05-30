#!/usr/bin/python3
"""define a class of square """


class Square():
    """initializing private using __size
    Attributes:
       __size (int): size of the quare
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
            self.__size = size

    def area(self):
        """Find area of square
        Returns: return the are of square
        """
        return self.__size ** 2
    
     def my_print(self):
        """Prints the square using '#' character.
           
           If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
