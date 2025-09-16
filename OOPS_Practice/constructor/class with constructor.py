
'''
Constructor - example
'''

class Student:
    def __init__(self,name,age,marks):
        print("calling Student Constructor")
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print(self.name,self.age,self.marks)


Student1=Student("John",23,"A")
Student1.display()