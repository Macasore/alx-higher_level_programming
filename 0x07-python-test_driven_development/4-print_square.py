#!/usr/bin/python3
"""Print Square module

This module contains a function used to print a square with the '#' character
"""


def print_square(size):
    """print_square function

    This function prints a square based on the size given

    Args:
         size (int): the only operand that determines it's size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
