
def decor_for_greet(func):
    def inner(name):
        if name=="Admin":
            print("#"* 35)
            print(f"Hello {name}, A very good Morning!")
            print("#" * 35)
        else:
            func(name)
    return inner


@decor_for_greet
def greet(name):
    print(f"Hello {name}! Good Morning!!!")

#greet("Vikas")
greet("Admin")