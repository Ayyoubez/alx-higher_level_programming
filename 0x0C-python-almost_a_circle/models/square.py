#!/usr/bin/python3
""" define a square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """

    def __init__(self, size, x=0, y=0, id=None):
        """ square init

        Args:
            size (int): size of the square side:
            x (int): position x
            y (int): position y
            id (int): square id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ gett / set size)"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self. *args, **kwargs):
        """Update the square

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif ar == 1:
                    self.size = arg
                elif ar == 2:
                    self.x = arg
                elif ar == 3:
                    self.y = arg
                ar += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ dictionary representation of square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ return the print and str rep of a square """
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                    self.width)
