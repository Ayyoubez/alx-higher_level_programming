#!/usr/bin/python3
""" define a base class"""
import json
import csv
from turtle import Turtle


class Base:
    """ definition class base

    The base class for all other classes in the project

    Private class Attribute:
        __nb_objects (int): number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor.

        Args:
            id (int): Base id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return Json file

        Args:
            list_dictionaries (list): a list of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Json Serialisation

        Args:
            list_objs (list): A list of inherited base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file1:
            if list_objs is None:
                file1.write("[]")
            else:
                list_dicts = [o.to_dictionaty() for o in list_objs]
                file1.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):

        """ deserialisation of Json

        Args:
            json_string (str): A json str
        Return:
            if json_string is none or empty
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ list of classes

        Args:
            cls (str): a class
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to csv file

        Args:
            list_objs (lis): list a Base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv1:
            if list_objs is None or list_objs == []:
                csv1.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv1, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ list of classes from json file

        Args:
            cls (list): csv file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv1:
                if cls.__name__ == "Reactangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fielnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv1, fieldnames=fieldnames)
                list_dicts = [dict([k, int(V)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw rectangle and square using Turtle class

        Args:
            list_rectangles (list): a list of rectangle obects
            list_square (list): a list of squares to draw
        """
        turtle = Turtle()
        turtle.screen.bgcolor("#3498db ")
        turtle.pensize(3)
        turtle.shape("turtle")
        turtle.color("green")
        for draw in list_rectangles:
            turtle.showturtle()
            turtle.up()
            turtle.goto(draw.x, draw.y)
            turtle.down()
            for i in range(2):
                turtle.forward(draw.width)
                turtle.left(90)
                turtle.forward(draw.height)
                turtle.left(90)
            turtle.hideturtle()
        turtle.color("white")
        for draw in list_squares:
            turtle.showturtle()
            turtle.up()
            turtle.goto(draw.x, draw.y)
            turtle.down()
            for i in range(2):
                turtle.forward(draw.width)
                turtle.left(90)
                turtle.forward(draw.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.exitonclick()
