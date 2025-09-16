

#__add__() method
# print(3+4)
# print((3).__add__(4))

# print("Hello "+"World")
# print("Hello ".__add__("world!"))

# list1=[3,5,6,7]
# list2=[1,4,5,6]
# print(list1+list2)
# print(list1.__add__(list2))

class Point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        new_a=self.x+other.x
        new_b=self.y+other.y
        return Point2D(new_a,new_b)

    def __str__(self):
        return f"({self.x} {self.y})"


pointA=Point2D(3,5)
print("PointA", pointA)
pointB=Point2D(3,6)
print("PointB", pointB)

print("Addition of two points ")
print(pointA+pointB)
