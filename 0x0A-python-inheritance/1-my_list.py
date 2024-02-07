#!/usr/bin/python3
""" Mylist class """


class MyList(list):
    """ built in class list """

    def print_sorted(self):
        """ print a list"""
        print(sorted(self))
