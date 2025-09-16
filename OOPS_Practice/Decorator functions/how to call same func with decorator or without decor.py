
def decor_for_add(func):
    def inner(a,b):
        print("#"*30)
        print("The Sum:",end='')
        print(func(a,b))
        print("#" * 30)
    return inner

#@decor_for_add
def add(a,b):
    print(a+b)
    return a+b

#result= add(10,30)

decor_add=decor_for_add(add)
decor_add(20,30)
add(20,30)


