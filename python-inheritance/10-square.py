#!/usr/bin/python3
"""Import BaseGeometry Class and Rectangle Subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "Class Square inhereting from Rectangle"
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
