'''
The __str__() method in Python is automatically called when you:

Use the print() function on an object
Call str(obj)
Use format(obj)

This method is typically overridden in custom classes to provide
a human-readable string representation of the object.
Without overriding __str__(), the default implementation (inherited from object)
returns a string showing the object’s type and memory address,
which is not very informative.
'''

class Point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"points coordinates are ({self.x},{self.y})"


point1=Point2D(4,5)
print(point1)

class Student:
    def __init__(self,name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade

    def __str__(self):
        return f"Student => name:{self.name} " \
               f"age:{self.age} " \
               f"grade:{self.grade }"


student_nora=Student("Nora",34,"A")
print(student_nora)