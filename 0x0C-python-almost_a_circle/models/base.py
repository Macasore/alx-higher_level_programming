#!/usr/bin/python3
"""Base module """


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """init function for initializing the class
        Args:
           id (int): the id attribute
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
