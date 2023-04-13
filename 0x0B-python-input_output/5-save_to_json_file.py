#!/usr/bin/python3
"""save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function
    function that writes an Object to a text file,
    using a JSON representation

    Args:
       my_obj (obj): the object operand
       filename (str): the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
