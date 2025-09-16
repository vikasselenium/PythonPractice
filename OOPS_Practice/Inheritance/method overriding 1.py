

class Parent:
   def method_1(self):
       print("inside parent version")

class Child(Parent):

    def method_1(self):
        print("inside child version")

parent=Parent()
parent.method_1() # calling on base version

child= Child()
child.method_1() # calling on child class

child_new=Child()



