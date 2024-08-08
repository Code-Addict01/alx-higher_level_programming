#!/usr/bin/python3
"""Defines function for JSON to object conversion"""
import json


def from_json_string(my_str):
    """Returns a python object representation of a JSON string"""
    return json.loads(my_str)
