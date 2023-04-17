#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
     Defines a rectangle object with
    width, height and x, y coordinates
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """instatiation function
        Constructor
        Call parent class constructor and initialises
        width, height, x and y values

        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """width getter"""
            return self.__width

        @width.setter
        def width(self, width):
            """width setter"""
            self.__width = width

        @property
        def height(self):
            """height getter"""
            return self.__height

        @height.setter
        def height(self, height):
            """height setter"""
            self.__height = height

        @property
        def x(self):
            """x getter"""
            return self.__x

        @x.setter
        def x(self, x):
            """x setter"""
            self.__x = x

        @property
        def y(self):
            """y getter"""
            return self.__y

        @y.setter
        def y(self, y):
            """y setter"""
            self.__y = y
