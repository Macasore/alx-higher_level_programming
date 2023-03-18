#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        for i in my_list:
            for j in my_list:
                if i >= j:
                    max = i
                    continue
                else:
                    max = j
                    break
        return max
