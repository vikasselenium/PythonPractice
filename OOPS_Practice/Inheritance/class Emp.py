
# example of Inheritance
class Employee:
    def __init__(self,name,age,address,phone):
        self.name=name
        self.age=age
        self.address=address
        self.phone=phone

# Below class inherits from Employee class

class Developer(Employee):
    def __init__(self, name,age,address, phone, programming_languages):
        Employee.__init__(self,name,age,address,phone)
        self.programming_languages=programming_languages


#class QA inherits from Employee
class QA(Employee):
    def __init__(self,name,age,address,phone,qa_skills):
        Employee.__init__(self,name,age,address,phone)
        self.qa_skills=qa_skills

dev1=Developer("ABC",34,"test address","878777777", ["java","python"])
print(dev1.name)
qa1=QA("XYZ",33,"test address2","8834343443",["Functional","automation"])
print(qa1.name)
