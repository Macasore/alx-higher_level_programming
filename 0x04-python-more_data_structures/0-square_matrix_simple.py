#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = []
    for i in matrix:
        yam = list((map(lambda x: x*x, i)))
        newlist.append(yam)
    return (newlist)
