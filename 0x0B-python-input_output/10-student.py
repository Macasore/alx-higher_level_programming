#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class
    This creates a blueprint for students
    """
    def __init__(self, first_name, last_name, age):
        """ instatiation function

        Args:
           first_name (str): the firstname parameter
           last_name (str): the lastname parameter
           age (int): the age parameter
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json function
        this function retrieves a dictionary representation
        of a Student instance
        """
        dicky = self.__dict__
        new_dict = {}
        if (isinstance(attrs, list)
           and all(isinstance(n, str) for n in attrs)):
            for i in attrs:
                if i in dicky.keys():
                    new_dict[i] = dicky[i]
                else:
                    continue
            return new_dict
        else:
            return dicky
