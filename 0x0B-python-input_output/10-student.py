#!/usr/bin/python3
"""Defines a Class Student"""


class Student:
    """define an instance student"""

    def __init__(self, first_name, last_name, age):
        """Instantiate a instance of Student

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrive a dictionary representation of Student

        If attrs is a list of strings, only retrieve attribute names
        contained in the list else retrieve all attributes
        
        Args:
            attrs (list): The attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
