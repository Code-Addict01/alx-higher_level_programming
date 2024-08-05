#!/usr/bin/python3
"""class square defining a square"""


class Square:
    """Define the square"""

    def __init__(self, size=0):
        """Initializing square
        Args:
            size (int): size of the sqaure
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size <= 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Return area of the square based on size"""
        return (self.__size ** 2)
