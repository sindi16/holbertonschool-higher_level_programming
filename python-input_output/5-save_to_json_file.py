#!/usr/bin/python3

"""module to write to  a file"""

import json


def save_to_json_file(my_obj, filename):
    """func to write to a file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
