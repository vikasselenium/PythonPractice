
#decorators are special functions that are used for decoration purpises
# that takes original function as argument, extend that functionality and returns the
#extended functionality

def decor_for_add(func):
    def inner(a,b):
        print("###########")
        print(a+b)
        print("###########")
    return inner

@decor_for_add
def add(a,b):
    return a+b

add(3,13)
