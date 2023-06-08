#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """MyList class

    This class is a subclass of list containing a function
    that prints the given list in an ascending order
    """
    def print_sorted(self):
        """print_sorted function

        this function prints the given list in a sorted order
        """
        newlist = self.copy()
        newlist.sort()
        print(newlist)
