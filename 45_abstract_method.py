from abc import ABC, abstractmethod
from math import pi 

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
     
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius

rect = rectangle(10,20)
cir = circle(5)

print("Rectangle")
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

print("\nCircle")
print("Area:", cir.area())
print("Perimeter:", cir.perimeter())

#shape = Shape()
# TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter