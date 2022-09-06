#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i == " ":
            print(" ", end="")

        elif i >= 97 and i <= 122:
            i = char(ord(i) - 32)
            print("{}".format(i), end="")
