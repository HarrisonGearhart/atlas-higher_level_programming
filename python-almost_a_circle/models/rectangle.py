#!/usr/bin/python3
"""Rectangle Class that inherets from Base Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class
    width and height attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
