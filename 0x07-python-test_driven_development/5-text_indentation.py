#!/usr/bin/python3
""" Text indentation module

This module contains a function that seperates a string based on
some special characters

"""


def text_indentation(text):
    """text_indentation function

    This function prints a text with two new lines after
    some special caracters

    Special characters - '.', '?', ':'

    Args:
       text (str): the text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.strip()
    special_characters = ['.', ':', '?']
    nextline = False
    for i, t in enumerate(new_text):
        if (t == ' ' and nextline is True):
            continue
        else:
            print(t, end="")
            nextline = False
        if t in special_characters:
            print("\n")
            nextline = True
