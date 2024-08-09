#!/usr/bin/python3
"""Defines a function that converts a class to JSON"""


def class_to_json(obj):
    """Return dictionary representation of simple data structure"""
    return obj.__dict__
