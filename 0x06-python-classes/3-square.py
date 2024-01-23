#!/usr/bin/python3

""" Square Module """


class Square:

    """ class constructor"""

    def __init__(self, size=0):
        """ initialistion of a square

        Args:
            size (int): the size of the side
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return the area of a square."""
        return ((self.__size) * (self.__size))
