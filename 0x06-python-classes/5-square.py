#!/usr/bin/python3

""" Square Module """


class Square:
    """ Square definition """

    def __init__(self, size=0):
        """ Sqaure Initialisation

        Args:
            size (int): the size of the square side
        """
        self.size = size

    @property
    def size(self):
        """ retrive the size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return area """
        return (self.__size * self.__size)

    def my_print(self):
        """ print the square with #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
