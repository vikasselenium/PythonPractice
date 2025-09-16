
def decor2_for_f(func):
    def inner2():
        print("decor 2 execution")
        func() # this will call inner 1
    return inner2


def decor1_for_f(func):
    def inner1():
        print("decorator 1 execution")
        func() # this will call original function
    return inner1


@decor2_for_f
@decor1_for_f
def f():
    print("original function")

f()




