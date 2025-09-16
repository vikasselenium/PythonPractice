

class Parent:
    surname="Galande"
    def __init__(self):
        print("Parent constructor")
    def f1(self):
        print("inside parent method")

class Child(Parent):
    def __init__(self):
        #super().__init__()
        print("Child constructor")
    def f2(self):
        print("inside a Child method")
        print("calling parent method")
        super().f1()

child1=Child()
# print(child1.surname)
#child1.f1()
child1.f2()