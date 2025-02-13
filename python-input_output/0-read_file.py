#!/usr/bin/python3

"""Module to implement a func"""


def read_file(filename=""):
    """Func that reads a file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
