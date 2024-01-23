#!/usr/bin/python3

"""Square Module """


class Square:
    """ Square class definition"""

    def __init__(self, size=0)
        """ constructor

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
