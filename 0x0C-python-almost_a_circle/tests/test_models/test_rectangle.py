#!/usr/bin/python3
""" unnitest for rectangle class"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_inst(unittest.TestCase):
    """ unittest for testing"""

    def test_rectangle(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_1_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_2_arg(self):
        rec1 = Rectangle(10, 5)
        rec2 = Rectangle(5, 10)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_3_arg(self):
        rec1 = Rectangle(4, 4, 8)
        rec2 = Rectangle(8, 8, 4))
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_2_arg(self):
        rec1 = Rectangle(1, 2, 3, 4)
        rec2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_5_arg(self):
        self.asserEqual(7, REctangle(10, 2, 0, 0, 7).id)

    def test_more_arg(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4, 5, 6)

