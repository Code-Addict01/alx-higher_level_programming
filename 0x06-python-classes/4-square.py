#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Define the square"""

    def __init__(self, size=0):
        """Init the square

        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return are of square based on size"""
        return (self.__size * self.__size)
