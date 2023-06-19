#!/usr/bin/python3
""" rectangle.py module"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class with parent class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.

        Arguments:
        ----------
        width [int] -- width of class.
        height [int] -- height of class.
        x [int] -- x of class, default = 0.
        y [int] -- y of class, default = 0.
        id [int] -- instance counter.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer ")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """getter method for height"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """computes the area of a Rectangle"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle using #"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method to updates instance attributes with */**args."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes with no-keyword & keyword args."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of this class."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
