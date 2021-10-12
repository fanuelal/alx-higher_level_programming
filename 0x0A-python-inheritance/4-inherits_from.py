#!/usr/bin/python3
"""This module defines the inherits_from function"""


def inherits_from(obj, a_class):
    """returns True or False based on inheritance"""
    if isinstance(obj, a_class) and type(obj):
        return True
    else:
        return False
