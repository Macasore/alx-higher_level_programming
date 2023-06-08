#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dictionary = sorted(a_dictionary.items())
    for key, value in b_dictionary:
        print("{}: {}".format(key, value))
