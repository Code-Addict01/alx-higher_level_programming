#!/usr/bin/python3
"""Defines a function that appends"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file

    Args:
        filename (str): Name of the file to append to.
        text (str): String to be appended
    Returns:
        Number of characters appended
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
