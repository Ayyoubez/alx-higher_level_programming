#!/usr/bin/python3
""" class inheriatance"""


def is_kind_of_class(obj, a_class):
    """ checker

    Args:
        obj (any): object to check
        a_class (type): the class
    return:
        if obj is exactly an instance
    """
    if isinstance(obj, a_class):
        return True
    return False
