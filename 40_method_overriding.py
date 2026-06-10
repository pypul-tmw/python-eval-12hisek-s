from math import pi 

class shape:
    def area(self):
        raise NotImplementedError

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class cylinder(circle):
    def __init__(self,radius,height):
        super().__init__(radius)
        self.height = height

    def area(self):
        base_area = super().area()
        return base_area * self.height

circle = circle(10)
cylinder = cylinder(10,20)
#print(circle.area())
print(cylinder.area())


"""
use of super():calls the parent constructor, so you don’t have to write:
super().method_nama(arg)
"""