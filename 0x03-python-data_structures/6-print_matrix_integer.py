#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) == 0:
            print("")
        for j, item in enumerate(i):
            if j != len(i) - 1:
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item))
