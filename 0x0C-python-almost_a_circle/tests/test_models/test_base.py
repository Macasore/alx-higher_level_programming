#!/usr/bin/python3
"""test_base file"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        """test_id function
        Tests that the logic for id works as
        expected i.e initialises object with id if specified
        or defaults to number of instances with default ids
        """
        base_0 = Base()
        base_1 = Base(1)
        base_2 = Base(8)
        base_3 = Base(2)

        # Assert their id values
        self.assertEqual(base_0.id, 1)
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 8)
        self.assertEqual(base_3.id, 2)

    def test_idnone(self):
        """test_idnone for empty id argument"""
        base_4 = Base()
        base_6 = Base()
        self.assertEqual(base_4.id, 2)
        self.assertEqual(base_6.id, 3)


if __name__ == "__main__":
    unittest.main()
