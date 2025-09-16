class Person:
    def __init__(name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

p = Person("Vikas", 30)
p.show()



class Student:
    def __init__(name, roll_no):
        self.name = name
        self.roll_no = roll_no

s = Student("Vikas", 101)
print(s.name)
