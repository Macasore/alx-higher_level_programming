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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, val):
        """width setter"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, hei):
        """height setter"""
        if type(hei) != int:
            raise TypeError("height must be an integer")
        if hei <= 0:
            raise ValueError("height must be > 0")
        self.__height = hei

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, val):
        """x setter"""
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, te):
        """y setter"""
        if type(te) != int:
            raise TypeError("y must be an integer")
        if te < 0:
            raise ValueError("y must be >= 0")
        self.__y = te

    def area(self):
        """this area function is for calculating
        the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """display
        prints the rectangle instance with the # character
        """
        for i in range(self.__y):
            print()
        for i in range(self.height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args):
        """ update
        updates the attributes of a rectangle instance
        """
        if len(args) == 1:
            for i in args:
                self.id = i
        elif len(args) == 2:
            self.id, self.__width = args
        elif len(args) == 3:
            self.id, self.__width, self.__height = args
        elif len(args) == 4:
            self.id, self.__width, self.__height, self.__x = args
        else:
            self.id, self.__width, self.__height, self.__x, self.__y = args

    def __str__(self):
        """str
        returns a string representation of the rectangle class
        """
        return ("[Rectangle] ("+str(self.id)+") "+str(self.__x)+"/"
                + str(self.__y)+" - "+str(self.__width)+"/"
                + str(self.__height))
