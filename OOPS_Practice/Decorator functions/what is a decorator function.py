
# decoration function is used for decoration purpose
# PVM will check of any decorator configured, it passes original function
# as an argument to decorator function,decorator function
# returns inner object, so inner function will be executed
# no of arguments should be same for inner() as well as original function
# without affecting original functionality we are adding extra functionality

# defn: decorator function takes function as argument, extend its functionality
# and returns a modified function with extended functionality
##

def decorator(func):
    print("Inside a decorator function ")
    def inner():
        print("Send a person to decorator")
        print("Show decorated person")
    return inner

@decorator
def show_person():
    print("Showing a person as it is")

show_person()