

def decor_for_add(func):
    def inner(a,b):
        print("#"*25)
        print("sum:",func(a,b))
        print("#" * 25)
    return inner

@decor_for_add
def add(a,b):
    return a+b

add(10,20)