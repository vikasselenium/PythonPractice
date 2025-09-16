
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    pass

class C(A):
    # def greet(self):
    #     #print("Hello from C")
    #     pass
    pass

class D(B,C):
    pass

obj=D()
obj.greet() #Hello from C