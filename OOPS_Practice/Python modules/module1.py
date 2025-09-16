

def add(a,b):
    print("Inside module1 - add function")
    print(f"sum is {a+b}")

def product(a,b):
    print("Inside module1 - product function")
    print(f"sum is {a*b}")



if __name__=='__main__':
    print(" Direct execution like main program")
    print(__name__)
    add(10, 20)
    product(30, 2)

else:
    print("Indirect execution because of import ")