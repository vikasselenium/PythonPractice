

def outer():
    print("Outer function execution started")

    def inner():
        print("Inner function execution")

    print("Outer function execution ended")
    return inner # function returns inner function object

f1=outer()
#print(f1)
f1() # inner function calling


