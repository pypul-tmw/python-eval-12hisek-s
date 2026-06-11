"""To define a property in Python, 
you use the built-in property function. 
The property function takes up to three arguments: 
the getter function, the setter function, and the deleter function (which is optional). 
"""
from abc import ABC, abstractmethod
from math import pi 

class shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass


class reactangle(shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


   

class circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0: 
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        return pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * pi * self.radius

"""
The key rule is:
Method → obj.method()
Property → obj.property (no parentheses)
"""

r = reactangle(4,9)
c = circle(5)
print(r.area) # insead of print(r.area())
print(r.perimeter)

print(c.area)
print(c.perimeter)