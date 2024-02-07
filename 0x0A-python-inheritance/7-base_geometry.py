#!/usr/bin/python3
""" base geometry """


class Basegeometry:
    """ base Geo"""

    def area(self):
        """ not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate as integer

        Args:
            name (str): name of parameter
            value (int): value of parameter
        raises:
            TypeError: if vale is not integer
            ValueEroor: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
