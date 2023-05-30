#!/usr/bin/python3
"""define a class of square """


class Square():
    """initializing private using __size
    Attributes:
       __size (int): size of the quare
    """
    def __init__(self, size):
        """assigning values to private attribute
        Args:
             size (int): size of a quare
        Returns: None
        """
        self.__size = size
