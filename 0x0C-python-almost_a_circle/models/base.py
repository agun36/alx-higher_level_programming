#!/usr/bin/python3
class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0  # private class attribute to track the number of objects

    def __init__(self, id=None):
        """
        Class constructor to initialize a new instance of the Base class.
        If an id is provided, assign it to the instance's id attribute.
        Otherwise, increment the __nb_objects count and assign the new value
        Args:
            id (int): The id for the instance (optional).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

