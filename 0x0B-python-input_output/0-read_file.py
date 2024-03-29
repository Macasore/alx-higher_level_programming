#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """read_file function

    reads the text in a file
    Args:
       filename (string): the file to be read
    """
    with open(filename, "r", encoding="UTF8") as myfile:
        for f in myfile.readlines():
            print(f, end="")
