#!/usr/bin/python3
"""Module: 1-rectangle
Defines a Ractangle class based on a previous class
"""


class Rectangle:
    """Class rectangle with width and height"""

    def __init__(self, width=0, height=0):
        """Initialization of Rectangle with instances

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving the width instance of rectangle"""
        return self.__width

    @property
    def height(self):
        """Retrieve height instance of rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of rectangle to a value

        Args:
            value: value of the width
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height of Rectangle to a value

        Args:
            value: value to be assigned to height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance

        Returns:
            Area of the rectangle based on height and width
        """

        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of Rectangle instance

        Returns:
            The perimeter of a rectangle from width and height
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns informal and nicely printed string representation
        of a Rectangle instance with # characters
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rect_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += '#'
            rect_str += '\n'
        return rect_str[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle to be able
        to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
