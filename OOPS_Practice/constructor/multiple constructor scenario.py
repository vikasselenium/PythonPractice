
class Student:

    # def __init__(self):
    #     print("one argument constructor")

    def __init__(self, name, age, grade): # python always consider latest constructor
        print("Multiple argument Constructor")
        self.name = name
        self.age = age
        self.grade = grade

    # def __init__(self):
    #     print("one argument constructor")


student_1 = Student()

student_2 = Student("John", 26, 90)
print(student_2.name, student_2.age, student_2.grade)

