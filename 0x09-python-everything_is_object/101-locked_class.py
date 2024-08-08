#!/usr/bin/python3
"""Class LockedClass"""


class LockedClass():
    """can't create new instance if not called 'first_name'"""

    __slots__ = ('first_name')
