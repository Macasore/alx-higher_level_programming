#!/usr/bin/python3
""" Add Item Module
This module contains code for alx input output
task 7
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]

j_file = None
filename = "add_item.json"
try:
    j_file = load_from_json_file(filename)
except Exception:
    j_file = []

newlist = []
newlist.extend(j_file)
newlist.extend(args)
save_to_json_file(newlist, filename)
