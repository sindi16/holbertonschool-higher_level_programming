#!/usr/bin/python3

"""module to load from a file"""

import json


def load_from_json_file(filename):
    """func to load from a file"""
    with open(filename, "r") as file:
        data = json.load(file)
        return data
