#!/usr/bin/python3

""" file writing function """


def write_file(filename="", text=""):
    """ write a text into a file.

    Args:
        filename (str): the name of the file.
        text (str): the text to write.
    Returns:
        the number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as file1:
        return file1.write(text)
