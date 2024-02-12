#!/usr/bin/python3
""" Integer addition function """


def add_integer(a, b=98):
    """ addition of a and b.

    floats are typecasted

    Raises:
        TypeError: if a or b is not integers or floats
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
