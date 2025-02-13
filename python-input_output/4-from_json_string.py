#!/usr/bin/python3

"""module to convert to python object"""

import json


def from_json_string(my_str):
    """func to convert to python object"""
    return json.loads(my_str)
