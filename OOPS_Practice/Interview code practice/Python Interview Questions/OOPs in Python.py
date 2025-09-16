# Encapsulation: wrapping up data and methods in class is encapsulation
# data abstraction: hiding complex implementation and only exposing essential details
# inheritance: Reusing code of parent class
# polymorphism: poly=> many and morphism means appearances
# same thing acts as differently e.g. + operator =, we can use it for adding 2 values
# as well as concatenating strings

from abc import ABC, abstractmethod

import math
class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        print("Parent class method")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calc_area(self):
        return math.pi*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def calc_area(self):
        return self.length*self.breadth


my_rectangle=Rectangle(12,3)
print(my_rectangle.calc_area())

my_circle=Circle(12)
print(my_circle.calc_area())
