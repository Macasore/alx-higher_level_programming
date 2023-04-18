#!/usr/bin/python3
"""Test file for rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle class

    """
    def test_rect(self):
        """test_rect function"""
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(2, 10)
        rect3 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(rect1.width, 2)
        self.assertEqual(rect2.height, 10)
        self.assertEqual(rect3.id, 5)





if __name__ == "__main__":
    unittest.main()
