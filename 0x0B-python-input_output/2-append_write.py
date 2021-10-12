#!/usr/bin/python3
"""this module is to create append_write function"""


def append_write(filename="", text=""):
    """"return the number of char add
    attribut(filename): Filename
    attribut(text): Text tha is add
    """
    with open(filename, 'a') as file:
        fileA = file.write(text)
    return len(text)
