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

        def area(self):
            """ return area """
            return (self.__size ** 2)

        @property
        def size(self):
            """ retrive the size """
            return self.__size

        @size.setter
        def size(self, value):
            """ set the size value """
            if not isinstance(value, int):
                 raise TypeError("size must be an integer")
            if value < 0:
                 raise ValueError("size must be >= 0")
            self.__size = value
