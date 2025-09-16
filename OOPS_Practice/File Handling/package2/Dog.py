#from package1.animal import Animal
#from package1.animal import *
#import package1.animal as animal
import package1.animal as animal
class Dog(animal.Animal):

    def __init__(self, name,color):
        super().__init__(name)
        self.color=color

    def speak(self):
        print(self.name, "Barks!")

d=Dog("Alita","Yellow")
print(d.color)

animal.animal_description()
print(animal.animal_test)

