from functools import reduce


def f1(func):
    func()
    print("Hello")

def f2():
    print("f2 function")

f1(f2)

# Filter function
list1=list(range(1,11))
print(list1)

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

filtered_list=list(filter(is_even,list1))
print(filtered_list)