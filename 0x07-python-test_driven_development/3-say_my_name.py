#!/usr/bin/python3
"""say_my_name module

This module prints a first name and a last name

"""


def say_my_name(first_name, last_name=""):
    """say_my_name function

    This function uses the first and last name passed into it
    to form a sentence.

    Args:
            first_name (str): The first parameter
            last_name (str): The second parameter
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
