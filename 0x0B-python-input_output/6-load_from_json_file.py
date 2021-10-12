#!/usr/bin/python3
"""this module is to create load_from_json_file"""


def load_from_json_file(filename):
    """returns the str from json"""
    with open(filename, 'r') as file:
        import json
        return json.loads(file)
