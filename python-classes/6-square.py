#!/usr/bin/python3
'''

Simple python file for createing a Square class
and its initiliazation with one private instance attribute
'''


class Square:
    '''

    Square class
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''

        Init method for square instances
        Args:
            size (int): Size of the square
        '''
        self.size = size
        self.position = position

    '''

    Property setter for attribute size
    '''

    @property
    def size(self):
        return self.__size

    '''
    Property decorator for getting position attrbiute
    '''

    @property
    def position(self):
        return self.__position

    '''
    Property decorator for setting position attribute
    '''

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) is False or len(value) != 2
           or (isinstance(value[0], int) is False or value[0] < 0)
           or (isinstance(value[1], int) is False or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    '''
    Property decorator for setting size attribute
    '''

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    '''

    Public instance method to calculate the area of the instance square
    '''

    def area(self):
        return self.size ** 2

    '''

    Instance method to print the area of the square
    '''

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for a in range(self.size):
                for i in range(self.position[0]):
                    print(" ", end="")
                for b in range(self.size):
                    print("#", end="")
                print()