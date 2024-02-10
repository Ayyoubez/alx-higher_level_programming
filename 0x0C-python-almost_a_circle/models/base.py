#!/usr/bin/python3
""" define a base class"""

class Base
    """ definition class base """
    __nb_objects = 0
    def __init__(self, id=None):
        """ class constructor.

        Args:
            id (int): Base id
        """
        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
