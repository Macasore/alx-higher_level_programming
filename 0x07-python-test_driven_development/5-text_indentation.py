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
    for i, t in enumerate(text):
        if t in ['.', ':', "?"]:
            print(t, end="")
            print("\n\n")
            continue
        elif (t == " " and text[i-1] in ['.', ':', "?"]):
            continue
        print(t, end="")
