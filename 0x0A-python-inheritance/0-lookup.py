#!/usr/bin/python3
""" lookup module
This module contains a function that returns the list of
available attributes and methods of an object:

"""


def lookup(obj):
    """ lookup function

    Args:
       obj: the object to be used
    """
    return dir(obj)
