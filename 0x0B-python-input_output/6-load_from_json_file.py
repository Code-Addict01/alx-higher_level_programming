#!/usr/bin/python3
"""Defines a function that created an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create a python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
