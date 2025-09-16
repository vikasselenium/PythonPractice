

class Parent:
    def __init__(self,age, name):
        self.age=age
        self.name=name

    def display(self):
        print(self.age)
        print(self.name)

class Child(Parent):
    def __init__(self,age,name,city):
        super().__init__(age,name)
        self.city=city

    def display(self):
        super().display()
        print(self.city)

child1=Child("56","ABC","Pune")
child1.display()