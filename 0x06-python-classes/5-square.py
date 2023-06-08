#!/usr/bin/python3

"""4-square module

This module contains a class definition of a square
with a private size attribute

"""


class Square:
    """This class contains the definition of a square


    """

    def __init__(self, size=0):
        """Initializes the square class

        Args:
             size (int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """	getter for size attribute

        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for size attribute

        Args:
             value (int): the size of the square

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """

        This function returns the area of a square

        """
        return self.__size * self.__size

    def my_print(self):
        """This function prints the square with the '#' character

        """
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                print("#" * self.__size)
