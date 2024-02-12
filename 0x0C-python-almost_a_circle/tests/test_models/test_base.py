#!/usr/bin/python3
""" unnitest for base.py

unittest classes:










"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_inst(unittest.TestCase):
    """ unitests for testing instantiations of class Base"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(15, Base(15).id)

    def test_instances_after_id(self):
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id(self):
        b = base(15)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_inst_private(self):
        with self.assertRaises(AttributeError):
            print(Base(15).__nb__instances)

    def test_str_id(self):
        self.assertEqual("Python",  Base("Python").id)

    def test_float_id(self):
        self.assertEqual(6.2, base(6.2).id)

    def test_coplex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.asserEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.asserEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_set_it(self):
        self.asserEqual({1, 2, 3} Base({1, 2, 3}.id)




