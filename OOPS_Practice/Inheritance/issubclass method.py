
# returns True if a class is sub-class of another class

class Animal:
    def __init__(self,age):
        self.age=age

class Dog(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.name=name

dog=Dog("nora",4)
print(dog.name)
print(dog.age)

print(issubclass(Dog,Animal))