#!/usr/bin/python3
"""Defines function that inserts a line of text in a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert line of text after each line containing a given string

    Args:
        filename (str): Name of the file
        search_string (str): string to search for in lines in the file
        new_string (str): The string to be inserted
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
