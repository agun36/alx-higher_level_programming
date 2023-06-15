#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of the Square class.
        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square (default: 0).
            y (int): The y-coordinate of the square (default: 0).
            id (int): The id of the square (optional).
        """
        super().__init__(size, size, x, y, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y        

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to the attributes."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def update(self, *args, **kwargs):
        """Update the attributes of the square."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
             for key, value in kwargs.items():
                 setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

      def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y, self.width)
