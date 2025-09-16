

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def find_diameter(self):
        diameter=self.radius*2
        return diameter

my_circle=Circle(5)
print(my_circle.find_diameter())