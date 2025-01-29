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

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """getter of the property"""
        return self.__size

    @size.setter
    def size(self, value):
        """methd to set the value of an attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Method to print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()