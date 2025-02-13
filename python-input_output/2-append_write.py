#!/usr/bin/python3

"""module to append to a file"""


def append_write(filename="", text=""):
    """func to append to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        data = file.write(text)
    return data
