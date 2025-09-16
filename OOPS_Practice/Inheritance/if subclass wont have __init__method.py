

class Polygon:
    def __init__(self,no_of_sides,color):
        self.no_of_sides=no_of_sides
        self.color=color

class Triangle(Polygon):
    pass

triangle1=Triangle(3,"red")
print(triangle1.no_of_sides)
print(triangle1.color)
