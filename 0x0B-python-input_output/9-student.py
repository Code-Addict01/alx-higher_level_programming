#!/usr/bin/python3
"""Defines a Class Student"""


class Student:
    """Defining the class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of a student instance

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary representation of the Student instance"""
        return self.__dict__
