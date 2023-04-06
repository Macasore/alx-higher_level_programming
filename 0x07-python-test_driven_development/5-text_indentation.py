#!/usr/bin/python3
"""Text Indentation Module
    This Module contains code for the text indentation task at ALX
"""


def text_indentation(text):
    """text_indentation function
        The text_indentation function prints a 2 new line characters
        when it encounters any of these characters ., ? and :
        Args:
                text (string): String containing text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    trimmed_text = text.strip()
    new_line = False
    delimeters = ['.', ':', '?']

    for c in trimmed_text:

        if new_line and c == ' ':
            # skip spaces at beginning of line
            continue
        else:
            new_line = False
            print(c, end="")

            # print 2 new lines if is delimeter
        if c in delimeters:
            print("\n")
            new_line = True
