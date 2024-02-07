#!/usr/bin/python3
""" class cheking """


def is_same_class(obj, a_class):
    """ checker

    Args:
        obj (any): object to check
        a_class (type): the class
    return:
        if obj is exactly an instance
    """
    if type(obj) == a_class:
        return True
    return False
