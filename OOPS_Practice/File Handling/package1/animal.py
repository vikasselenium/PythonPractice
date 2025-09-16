
animal_test="Animal_test"

class Animal:
    legs=4
    def __init__(self,name):
        self.name=name

    def speaks(self,name):
            print(self.name, " makes sound")

def animal_description():
    print(f"{animal_test}Animals should make sound and move")

