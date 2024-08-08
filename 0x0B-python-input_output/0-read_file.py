#!/usr/bin/python3
"""Defines a function that reads a text-file"""


def read_file(filename=""):
    """Print content of UTF8 encoded file to the stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
