

def decor2_for_num(func):
    def inner2():
        x=func() # inner1 will return 400
        return x*2
    return inner2 # inner2 will return 400*2 i.e. 800 --always draw a diagram


def decor1_for_num(func):
    def inner1():
        x=func()
        return x*x
    return inner1

@decor1_for_num
@decor2_for_num
def num():
    return 20

print(num())