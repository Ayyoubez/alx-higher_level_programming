#!/usr/bin/python3

""" Square Module """


class Square:
    """ Square definition """

    def __init__(self, size=0):
        """ Sqaure Initialisation

        Args:
            size (int): the size of the square side
        """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

    @property
    def area(self):
        """ return area """
        return (self.__size ** 2)

    def size(self):
        """ retrive the size """
        return self.__size

    def size(self, value):
        """ set the size value """
        self.__size = value
