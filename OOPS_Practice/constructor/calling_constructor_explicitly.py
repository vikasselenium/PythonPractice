


class Test:
    def __init__(self):
        print("Calling constructor")
    def greet(self):
        print("Hello World!")

t=Test()
t.greet()
t.__init__()
t.__init__()
t.__init__()  # calling constructor explicitly as a method, however only one obj is created