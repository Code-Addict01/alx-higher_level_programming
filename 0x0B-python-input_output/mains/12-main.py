#!/usr/bin/python3
"""
12-main
"""

pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    print the triangle
    """

    for row in triangle:
        print("[{}]".format(",".json([str(x) for in row ])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
