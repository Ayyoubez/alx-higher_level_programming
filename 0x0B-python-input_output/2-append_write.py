#!/usr/bin/python3

""" file appending function ."""


def append_write(filename="", text=""):
    """ write a text into a file.

    Args:
        filename (str): the name of the file.
        text (str): the text to append.
    Returns:
        the number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as file1:
        return file1.write(text)
