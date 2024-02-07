#!/usr/bin/python3
""" inherited class function"""


def inherits_from(obj, a_class):
    """ checker

    Args:
        obj (any): object to check
        a_class (type): the class
    return:
        if obj is exactly an instance
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
