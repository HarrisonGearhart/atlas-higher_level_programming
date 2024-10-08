#!/usr/bin/python3
"""Create an class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class
    attribute area
    raise exception is not emplemented
    method to validate value
    raise typeerror is value isnt integer
    raise valueerror if int isnt positive"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
	"""Rectangle class that inherits from BaseGeometry"""
	def __init__(self, width, height):
		self.integer_validator("width", width)
		self.integer_validator("height", height)
		self.__width = width
		self.__height = height
