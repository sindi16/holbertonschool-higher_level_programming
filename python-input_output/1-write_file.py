#!/usr/bin/python3

"""module to write a file"""

def write_file(filename="", text=""):
    """func to write a file"""
    with open(filename, "w", encoding="utf-8") as file:
        data = file.write(text)
    return(data)