from abc import ABC, abstractmethod
from dataclasses import dataclass 
from math import pi



class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    

@dataclass
class rectangle(shape):
    width : float
    height : float

    def area(self):
        return self.width * self.height

@dataclass
class circle(shape):
    radius : float

    def area(self):
        return pi * self.radius ** 2


r = rectangle(width = 4,height = 9)
c = circle(radius= 5)

print(r.area())
print(c.area())







"""
----Without a dataclass:

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

----With a dataclass:

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    salary: float
"""