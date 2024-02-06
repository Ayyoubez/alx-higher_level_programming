#!/usr/bin/python3
""" Class student """


class Student:
    """ class student """

    def __init__(self, first_name, last_name, age):
        """ initialise new student

        Args:
            first_name (str): first name
            last_name (sytr): last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dict representaion

        Args:
            attrs (list): attributes
        """
        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__
