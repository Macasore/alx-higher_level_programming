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

    def to_json(self):
        """to_json function
        this function retrieves a dictionary representation
        of a Student instance
        """
        return self.__dict__
