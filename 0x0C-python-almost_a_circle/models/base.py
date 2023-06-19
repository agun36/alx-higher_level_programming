#!/usr/bin/python3
""" base.py module """
import json
import csv


class Base():
    """ My base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as wf:
            if list_objs is None:
                wf.write("[]")
            else:
                list_d = [o.to_dictionary() for o in list_objs]
                wf.write(cls.to_json_string(list_d))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(5, 9)
            else:
                new = cls(6)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes a object's list string representation
        into a CVS file
        """
        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', encoding='utf-8') as file:
            string = csv.writer(file)

            if cls.__name__ == "Square":
                for i in list_objs:
                    string.writerow([i.id, i.size, i.x, i.y])
            elif cls.__name__ == "Rectangle":
                for i in list_objs:
                    string.writerow([i.id, i.width, i.height, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        reads from a CVS file an object's list
        string representation.
        """
        filename = cls.__name__ + ".csv"
        mylist = []

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                read = csv.reader(file)
                for i in read:
                    if cls.__name__ == "Square":
                        dict1 = {
                            "id": int(i[0]), "size": int(i[1]),
                            "x": int(i[2]), "y": int(i[3])
                            }
                    elif cls.__name__ == "Rectangle":
                        dict1 = {
                            "id": int(i[0]), "width": int(i[1]),
                            "height": int(i[2]), "x": int(i[3]),
                            "y": int(i[4])
                            }
                    mylist.append(cls.create(**dict1))
            return mylist
        except Exception:
            return []
