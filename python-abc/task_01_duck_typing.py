from abc import ABC
import math

class Shape(ABC):
    @abstractmethod
    def area(Shape):
        pass
    @abstractmethod
    def perimeter(Shape):
        pass
    
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        
        def area(self, radius):
                return math.pi * self.radius**2

        def perimeter(self, radius):
            return 2*math.pi * self.radius
        
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2(self.width + self.height)

    def shape_info(shape):
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
