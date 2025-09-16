
# we can define/declare one function inside another function in Python
# this is nothing but called as nested functions

def outer():
    print("Outer function execution started")
    def inner():
        print("Inner function execution")
    #inner() # we are calling inner function
    #inner()
    #inner()
    print("Outer function execution ended")

outer() # here we didn't called inner() function
#inner() #NameError: name 'inner' is not defined.


