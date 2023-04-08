#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger class

    This class contains test cases used to test the
    '6-max_integer' module.
    """

    def test_allpositive(self):
        """test_allpositive function

        checks when all are positive
        """
        self.assertEqual(max_integer([1, 4, 54, 5, 3]), 54)

    def test_somenegative(self):
        """test_somenegative function

        checks when some are negative
        """
        self.assertEqual(max_integer([-2, 3, -4, 5]), 5)

    def test_none(self):
        """test_none function

        checks when the list is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_similarmax(self):
        """test_similarmax function

        checks when there are more than one max integer
        """
        self.assertEqual(max_integer([1, 4, 4, 2]), 4)

    def test_none1(self):
        """test_none1 function

        checks when the list is empty
        """
        self.assertEqual(max_integer(), None)

    def test_just1(self):
        """test_just1 function

        checks when the list contains only one value
        """
        self.assertEqual(max_integer([4]), 4)
