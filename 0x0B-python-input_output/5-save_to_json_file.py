#!/usr/bin/python3
""" JSON file writing funtuion """
import json


def save_to_json_file(my_obj, filename):
    """ write an object to a text with sjon"""
    with open(filename, "w") as file1:
        json.dump(my_obj, file1)
