#!/usr/bin/python3
"""function that returns the dictionary description with simple data structure
list, dictionary, string, integer and boolean for JSON serialization of object
"""


def class_to_json(obj):
    """returns dictionary description"""
    return obj.__dict__
