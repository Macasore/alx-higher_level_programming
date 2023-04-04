#!/usr/bin/python3
""" Add integer module

This module contains the function that adds two integers

"""


def add_integer(a, b=98):
    """add_integer function

    This function adds two integers and returns the result

    Args:
            a (int): first integer
            b (int): second interger
    """
    if (type(a) not in [int, float]):
        raise TypeError("a must be an integer")

    elif (type(b) not in [int, float]):
        raise TypeError("b must be an integer")

    else:
        a, b = int(a), int(b)
        return a + b
