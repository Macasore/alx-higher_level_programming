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

    def test_widthtype(self):
        """test_widthtype
        this is for testing the input type of width
        """
        rect5 = Rectangle(2, 5, 6, 7, 4)
        with self.assertRaises(TypeError) as context:
            rect5.width = "5"

        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect5.width = 10.4

        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect5.width = None

        self.assertTrue("width must be an integer" in str(context.exception))

    def test_widthvalue(self):
        """test_widthvalue
        this is to test the value
        """
        rect5 = Rectangle(2, 5, 6, 7, 4)
        with self.assertRaises(ValueError) as context2:
            rect5.width = 0
        self.assertTrue("width must be > 0" in str(context2.exception))

        with self.assertRaises(ValueError) as context3:
            rect5.width = -4
        self.assertTrue("width must be > 0" in str(context3.exception))

    def test_heighttype(self):
        """test_heighttype
        this is for testing the input type of height
        """
        rect5 = Rectangle(2, 5, 6, 7, 4)
        with self.assertRaises(TypeError) as context:
            rect5.height = "5"

        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect5.height = 10.4

        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect5.height = None

        self.assertTrue("height must be an integer" in str(context.exception))

    def test_heightvalue(self):
        """test_heightvalue
        this is to test the value
        """
        rect5 = Rectangle(2, 5, 6, 7, 4)
        with self.assertRaises(ValueError) as context2:
            rect5.height = 0
        self.assertTrue("height must be > 0" in str(context2.exception))

        with self.assertRaises(ValueError) as context3:
            rect5.height = -4
        self.assertTrue("height must be > 0" in str(context3.exception))

    def test_xtype(self):
        """test_xtype
        this is for testing the input type of x
        """
        rect5 = Rectangle(2, 5, 6, 7, 4)
        with self.assertRaises(TypeError) as context:
            rect5.x = "5"

        self.assertTrue("x must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect5.x = 10.4

        self.assertTrue("x must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect5.x = None

        self.assertTrue("x must be an integer" in str(context.exception))

    def test_xvalue(self):
        """test_xvalue
        this is to test the value
        """
        rect5 = Rectangle(2, 5, 6, 7, 4)
        with self.assertRaises(ValueError) as context2:
            rect5.x = -3
        self.assertTrue("x must be >= 0" in str(context2.exception))

        with self.assertRaises(ValueError) as context3:
            rect5.x = -4
        self.assertTrue("x must be >= 0" in str(context3.exception))

    def test_ytype(self):
        """test_ytype
        this is for testing the input type of y
        """
        rect5 = Rectangle(2, 5, 6, 7, 4)
        with self.assertRaises(TypeError) as context:
            rect5.y = "5"

        self.assertTrue("y must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect5.y = 10.4

        self.assertTrue("y must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect5.y = None

        self.assertTrue("y must be an integer" in str(context.exception))

    def test_yvalue(self):
        """test_yvalue
        this is to test the value
        """
        rect5 = Rectangle(2, 5, 6, 7, 4)
        with self.assertRaises(ValueError) as context2:
            rect5.y = -1
        self.assertTrue("y must be >= 0" in str(context2.exception))

        with self.assertRaises(ValueError) as context3:
            rect5.y = -4
        self.assertTrue("y must be >= 0" in str(context3.exception))
        rect5.y = 0
        self.assertEqual(rect5.y, 0)

    def test_area(self):
        """test_area
        tests the area function
        """
        rect7 = Rectangle(3, 2)
        rect8 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect7.area(), 6)
        self.assertEqual(rect8.area(), 56)


if __name__ == "__main__":
    unittest.main()
