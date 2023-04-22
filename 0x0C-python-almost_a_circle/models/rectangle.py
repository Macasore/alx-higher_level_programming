#!/usr/bin/python3
""" Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class
    Defines a rectangle object with
    width, height and x, y coordinates
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor
        Call parent class constructor and initialises
        width, height, x and y values
        """
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function for __width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for __width property
        Validates width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter function for __height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for __height property
        Validates and sets the height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter function for __x property
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function for __x property
        Validates x value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter function for __y property
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for __y property
        Validates y value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    # Public instance Methods

    def area(self):
        """area function
        Returns the area of the rectangle instance
        """

        return self.__width * self.__height

    def display(self):
        """display function
        Prints the rectangle to stdout using #
        """

        # Single row of entire rectangle
        row = f"{self.__x * ' '}{self.__width * '#'}\n"

        # Full rectangle with position factored in
        result = "{}{}".format(self.__y * "\n", row * self.__height)

        print(result, end="")

    def __str__(self) -> str:
        """string representation function
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update function
        Updates rectangle attributes in the order
        id, width, height, x, y
        keyword args are also allowed
        """
        # List of instance attributes in the order they are passed as *args
        attr_keys = ["id", "width", "height", "x", "y"]

        # Set attributes based on the no keyword args
        for index, arg in enumerate(args):
            self.__setattr__(attr_keys[index], arg)

        # If args is not empty, skip kwargs
        if len(args) != 0:
            return

        for key, value in kwargs.items():
            if key in attr_keys:
                self.__setattr__(key, value)

    def to_dictionary(self):
        """to_dictionary function
        Converts rectangle instance to a
        dictionary representation of the instance
        """
        # Attribute keys
        attr_keys = ["id", "width", "height", "x", "y"]

        # Define new dictionary and assign keys with the corresponding values
        dic = {}

        for key in attr_keys:
            dic[key] = self.__getattribute__(key)

        return dic
