#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, width):
            self.__height = height

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, width):
            self.__x = x

        @property
        def y(self):
            return self.__y

        @y.setter
        def width(self, width):
            self.__y = y
