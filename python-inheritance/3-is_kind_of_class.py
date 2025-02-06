#!/usr/bin/python3
"""Module to return if specific cond is met"""


def is_kind_of_class(obj, a_class):
    """Func to check specific requirement"""
    if isinstance(obj, a_class):
        return True
    return False
