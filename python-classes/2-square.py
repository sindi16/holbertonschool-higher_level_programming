#!/usr/bin/python3
#!/usr/bin/python3

"""module about a class in python"""


class Square:
    """the class Square"""
    def __init__(self, size=0):
        """func to initialize objects"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
