#!/usr/bin/python3
"""Define a class called Square with a size attribute.
Size must an integer >= 0.
Raise errors if the user input is invalid
Returns the current area of the square"""


class Square:
    """Square defined by its size
    raises exceptions
    returns the current area"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
