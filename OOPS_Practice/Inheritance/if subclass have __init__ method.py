
# when using super() method-> self passed automatically
# when using classname-> we need to pass self as a parameter

class Polygon:
    def __init__(self,no_of_sides,color):
        self.no_of_sides=no_of_sides
        self.color=color

class Triangle(Polygon):
    No_of_sides=3
    def __init__(self,base,height,color):
        super().__init__(Triangle.No_of_sides,color)
        #Polygon.__init__(self,Triangle.No_of_sides, color)
        self.base=base
        self.height=height


triangle1=Triangle(3,5,"Red")
print(triangle1.no_of_sides)
print(triangle1.color)
print(triangle1.base)
print(triangle1.height)
