#!/usr/bin/python3

""" file reading function """


def read_file(filename=""):
    """ print the content of a file in stdout """
    with open(filename, encoding="utf-8") as file1:
        print(file1.read(), end="")
