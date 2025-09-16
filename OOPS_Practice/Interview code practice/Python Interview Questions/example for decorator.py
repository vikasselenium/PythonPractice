
# sample decorator function

def decor_for_add(func):
    def inner(a,b):
        print("####Adding two numbers###")
        print(func(a,b))
        print("####end###################")
    return inner

@decor_for_add
def add(a,b):
    return a+b

add(2,3)