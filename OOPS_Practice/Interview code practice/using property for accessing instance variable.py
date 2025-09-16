
# Example showing property usage
# we can access instance variables as class attributes
# without calling for getter and setter method
class Employee:
    def __init__(self,sal):
        self._sal=sal

    @property
    def sal(self):
        return self._sal

    @sal.setter
    def sal(self,new_value):
        if new_value > 0:
            self._sal=new_value

e1 = Employee("2000")
print(e1.sal)
e1.sal=45000
print(e1.sal)

