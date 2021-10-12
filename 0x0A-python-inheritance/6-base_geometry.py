#!/usr/bin/python3
"""this module creates a class named BaseGeometry"""


class BaseGeometry:
        """An class named BaseGeometry
    Attributes:
    attr1(area): Raises an exception
    """
        def area(self):
            """raise an exception"""
            raise Exception("area() is not implemented")
