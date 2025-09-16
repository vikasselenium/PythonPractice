import math

# dir() ==>> list out all members of current module
# dir(module_name) ==> to list out of all members of specified module

x=888
y=999

def add(a,b):
    return a+b

class Test:
    pass

print(dir())
# ['Test', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'x', 'y']
# interpreted adds all this predefined members required for internal purpose
print(dir(math))

# what is difference between dir() and help() function
# if we want to get  explanation/documentation about members => help(math)
print(help(math))
