#!/usr/bin/python3
""" Rectangle inherits from Bsegeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle inherit BaseGeo"""

    def __init(self, width, height):
        """ initialisation

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
