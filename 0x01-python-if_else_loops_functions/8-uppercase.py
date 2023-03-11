#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for i in str:
        if ord(i) >= ord("a"):
            upper_str += chr(ord("A") + (ord(i) - ord("a")))
        else:
            upper_str += i
    print("{}".format(upper_str))
