
def greet(name):
    print("Good Morning!", name)


wish=greet # function aliasing
print(id(wish))
print(id(greet))

wish("Vikas")
greet("Aryan")
del wish
greet("Ranjana")
