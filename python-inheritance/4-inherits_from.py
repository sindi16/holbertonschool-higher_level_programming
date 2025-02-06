#!/usr/bin/python3

"""Module to checks specific req"""


def inherits_from(obj, a_class):
    """Func to check req"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
