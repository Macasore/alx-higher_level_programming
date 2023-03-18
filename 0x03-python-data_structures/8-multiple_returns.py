#!/usr/bin/python3
def multiple_returns(sentence):
    a = [0, 0]
    if sentence == "":
        a[1] = None
    else:
        a[0] = len(sentence)
        a[1] = sentence[0]
    return tuple(a)
