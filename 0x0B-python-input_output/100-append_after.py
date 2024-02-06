#!/usr/bin/python3
""" text file insert function """


def append_after(filename="", search_string="", new_string=""):
    """ insert text after ech line

    Args:
        filename (str): file name
        search_string (str): search within the file
        new_string (str): string to insert
    """

    txt = ""
    with open(filename) as file1:
        for line in file1:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as file2:
        file2.write(txt)
