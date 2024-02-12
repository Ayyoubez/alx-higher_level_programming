#!/usr/bin/python3
""" max integer module"""


def max_integer(list=[]):
    """ function to find the max integer"""

    if len(list) == 0:
        return None
    res = list[0]
    i = 0
    while i < len(list):
        if list[i] > res:
            res = list[i]
        i += 1
    return res
