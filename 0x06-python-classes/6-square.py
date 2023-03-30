#!/usr/bin/python3

"""6-square module

This module contains a class definition of a square
with private attributes

"""


class Square:
    """This class contains the definition of a square


    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square class

        Args:
             size (int): the size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter function for the position

        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter function for the position attribute

        Args:
             value (int): the position of the square

        """
        if len(value) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#"*self.__size)
