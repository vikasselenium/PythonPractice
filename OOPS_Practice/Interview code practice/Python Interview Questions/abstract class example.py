
# we can have constructor in abstract class, even we don't initialize it
# abstract class have abstract method, where child class needs to
# implement it
# end user dont need to know like how area is calculated, however they
# know like there is area() method that they can use

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth


rectangle1=Rectangle(10,30)
print(rectangle1.area())
