class EMP:
    def __init__(self,age,name):
        self._age=age
        self.name=name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,newage):
        self._age=newage


e=EMP(12,"ABC")
print(e.age)

a = {1, 2, 3}
b = {3, 4, 5}

#union, intersection, difference
