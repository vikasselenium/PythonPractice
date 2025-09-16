import math
from abc import ABC,  abstractmethod


#Abstraction: Abstract class hides implementation details
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Encapsulation: Private attributes with controlled access
class Rectangle(Shape):
    def __init__(self,length, breadth):
        self._length=length
        self._breadth=breadth
        # we are restricting access to instance variable directly from outside

    def area(self):
        return self._length*self._breadth

class Circle(Shape):
    def __init__(self,radius):
        self._radius=radius

    def area(self): #Polymorphism
        return math.pi* self._radius ** 2

shapes=[Rectangle(12,3), Circle(4)]

for s in shapes:
    print(s.area())


