#!/usr/bin/python3
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
