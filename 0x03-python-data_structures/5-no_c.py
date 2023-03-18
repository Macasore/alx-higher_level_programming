#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for i in my_string:
        if i.lower() != "c":
            newstring += i
    return newstring
