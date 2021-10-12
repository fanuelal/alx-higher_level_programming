#!/usr/bin/python3
"""This module defines the write_file function"""


def write_file(filename="", text=""):
    """write a file
    Args:
      filename(str): Filename
      text(str): Text written on file
    """
    with open(filename, 'w') as file:
        fileW = file.write(text)
        file.close
    return len(text)
