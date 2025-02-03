#!/usr/bin/python3

'''
    Simple module for creating a
    Rectnagle class with instance methods
    and class methods
'''


class Rectangle:
    '''
        Rectangle class with two attributes

    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
            Init function for Rectangle class

        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''
            Width attribute getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Width attribute setter
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
            Height attribute getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Height attribute setter
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
            Instance method to calculate
            the area of a rectangle
        '''
        return self.width * self.height

    def perimeter(self):
        '''
            Instance method to calculate the
            perimeter of the rectangle
        '''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        '''
            Method for printing our instances
            in a represantive way
        '''
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            for j in range(self.width):
                string += str(self.print_symbol)
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        '''
            Method for printing the
            represantation of our object
            as its initialization
        '''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''
            Instance method to print a message
            when an instance is deleted
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
