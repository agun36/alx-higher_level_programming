s is the Base module.
Contains the Base class which will be the
“base” of all other classes in this project.
"""
import json
import csv
import turtle


class Base():
    """This class will be the “base” of all other classes in this project.
    The goal is to manage id attribute in all our future classes
    and to avoid duplicating the same code and same errors.
    Attributes:
        __nb_objects (int): the number of created Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the default attributes of the Base object.
        Args:
            id (int): the identifier of the Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): a list of objects.
        """
        lst = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of the JSON string representation to json_string.
        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            dictionary (dict): the values of the wanted instance.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                json_file = Base.from_json_string(f.read())
                return [cls.create(**dct) for dct in json_file]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the CSV string representation of list_objs to a file.
        Args:
            list_objs (list): a list of objects.
        """
        loaded = []
        with open(cls.__name__ + ".csv", 'w') as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write('[]')
            else:
                if cls.__name__ is "Rectangle":
                    loaded = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    loaded = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=loaded)
                for list_obj in list_objs:
                    writer.writerow(list_obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes the CSV string representation
        of list_objs from a file.
        """
        loaded = []
        try:
            with open(cls.__name__ + ".csv", 'r') as f:
                if cls.__name__ is "Rectangle":
                    loaded = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    loaded = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames=loaded)
                dicts = [dict([k, int(v)] for k, v in l.items())
                        for l in reader]
                return [cls.create(**dct) for dct in dicts]

        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.
        Args:
            list_rectangles (list): a list of rectangle instances.
            list_squares (list): a list of square instances.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor('#000000')
        turt.shape('turtle')
        turt.color('#ffffff')
        turt.penup()
        turt.goto(-200, 200)
        for rect in list_rectangles:
            turt.goto(turt.xcor() + (rect.width + 20), turt.ycor() - (rect.height + 20))
            turt.up()
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.penup()

        turt.goto(-200, -20)
        for squares in list_squares:
            turt.goto(t.xcor() + (squares.width + 20), turt.ycor() - (squares.height + 20))
            turt.up()
            turt.down()
            for i in range(2):
                turt.forward(squares.width)
                turt.left(90)
                turt.forward(squares.height)
                turt.left(90)
            turt.penup()
        turt.Screen().exitonclick()
