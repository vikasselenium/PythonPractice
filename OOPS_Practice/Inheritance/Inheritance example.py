

class Employee:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal

class Developer(Employee):
    def __init__(self,name,age,sal,programming_skills):
        super().__init__(name,age,sal)
        self.programming_skills=programming_skills

python_dev=Developer("ABC",35,40000,["Python","Pytest"])
print(python_dev.name)
print(python_dev.programming_skills)