#!/usr/bin/python3
""" JSON file reading """
import json


def load_from_json_file(filename):
    """ create a python object from JSON file"""
    with open(filename) as file1:
        return json.load(file1)
