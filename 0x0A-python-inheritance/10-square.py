#!/usr/bin/python3
'''defining square class'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size):
        '''initialization of square object'''
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """get the area of a square"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
