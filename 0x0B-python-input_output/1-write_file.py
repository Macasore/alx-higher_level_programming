#!/usr/bin/python3
"""1-write_file module"""


def write_file(filename="", text=""):
    """write_file function
   this is a function that writes a string to a text file
   and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
