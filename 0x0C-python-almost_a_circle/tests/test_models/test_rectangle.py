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

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
