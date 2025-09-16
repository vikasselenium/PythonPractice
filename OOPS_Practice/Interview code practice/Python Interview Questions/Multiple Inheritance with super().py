class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super().show()  # Calls next in MRO

class C(A):
    def show(self):
        print("Class C")
        super().show()  # Calls next in MRO

class D(B, C):
    def show(self):
        print("Class D")
        super().show()  # Calls next in MRO

obj = D()
obj.show()
