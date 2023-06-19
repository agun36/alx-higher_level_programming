#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of the Square class.
        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square (default: 0).
            y (int): The y-coordinate of the square (default: 0).
            id (int): The id of the square (optional).
        """
        super().__init__(size, size, x, y, id)  # Call the constructor of the Rectangle class

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
