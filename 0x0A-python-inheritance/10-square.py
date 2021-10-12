#!/usr/bin/python3
"""This module creates a Square class that inherts from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """A class named BaseGeometry
    Attributes:
    attr1(size): width of square
    """
    def __init__(self, size):
        """initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
    def area(self):
        """return the area of square"""
        return self.__size ** 2
    def __str__(self):
        """returns string representation"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
        
