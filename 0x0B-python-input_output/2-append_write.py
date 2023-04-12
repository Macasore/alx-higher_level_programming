#!/usr/bin/python3
""" append_write module"""


def append_write(filename="", text=""):
    """append_write function
    this function that appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as k:
        return k.write(text)
