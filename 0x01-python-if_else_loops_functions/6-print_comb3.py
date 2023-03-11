#!/usr/bin/python3
a = []

for i in range(10):
    for j in range(10):
        if "{}{}".format(j, i) in a:
            continue
        else:
            if i == j:
                continue
            elif "{}{}".format(i, j) == "89":
                print("{}{}".format(i, j))
            print("{}{}".format(i, j), end=", ")
            a.append("{}{}".format(i, j))
