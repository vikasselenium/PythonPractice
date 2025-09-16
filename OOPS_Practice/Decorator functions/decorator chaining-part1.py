# we can add multiple decorators for same function
# all these decorators will form decorator chaining

def decor2_for_f(func):
    def inner2():
        print("Decorator 2 execution")
    return inner2

def decor1_for_f(func):
    def inner1():
        print("Decorator 1 execution")
    return inner1

@decor2_for_f
@decor1_for_f
def f():
    print("Original function")

f() # original function will be passed to decor2->inner1 will be passed to decor2->inner2