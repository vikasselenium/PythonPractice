
# using base class method in all child class
class Polygon:
    def __init__(self,no_of_sides, color):
        self.no_of_sides=no_of_sides
        self.color=color
    def describe_polygon(self):
        print(f"no of sides:{self.no_of_sides} and color is {self.color}")

class Triangle(Polygon):
    no_of_sides=3
    def __init__(self,color,base,height):
       Polygon.__init__(self,Triangle.no_of_sides,color)
       self.base=base
       self.height=height

    def find_area(self):
       return (self.base*self.height)/2

class Square(Polygon):
    no_of_sides=4
    def __init__(self,side_len,color):
        Polygon.__init__(self,Square.no_of_sides,color)
        self.side_len=side_len

    def find_area(self):
        return self.side_len**2


my_triangle=Triangle("red",12,4)
my_triangle.describe_polygon()

my_square=Square(12,"Green")
my_square.describe_polygon()

print(my_triangle.find_area())
print(my_square.find_area())