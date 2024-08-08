#!/usr/bin/python3
"""Defines function that converts string to JSON"""
import json


def to_json_string(my_obj):
    """Returns a JSON representation of an object (string)"""
    return json.dumps(my_obj)
