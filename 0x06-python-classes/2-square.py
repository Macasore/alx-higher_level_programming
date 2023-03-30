#!/usr/bin/python3

"""
This module contains the class definition of a square

"""


class Square:
    """
    This is a class that defines a square.
    """
    def __init__(self, size=0):
        """
        This function initializes a square object with a private attribute
        'size'and returns a Typeerror if it isn't an integer and
        a ValueError if it's less than zero

        Args:
             size (int): size of a square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
