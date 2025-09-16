#variable length arguments
def func(*args):
    return sum(args)

print(func(10,20,30,40))

def func_kw(**kwargs):
    for k,v in kwargs.items():
        print(f"key:{k}, value:{v}")

func_kw(fname="Vikas", lname="Galande")

x="global"

def func():
    x="local"
    print(x)

print(x)
func()

#shallow copy
# deep copy

import copy

x=[[10,20],"Vikas"]
shallow_x=copy.copy(x)
shallow_x[0][0]=20
print(x)

deep_copy=copy.deepcopy(x)
deep_copy[0][0]=30
print(deep_copy)
print(x)

#iterable represents stream of data
# implements __itr__() and next method

my_list=[20,30,40]
itr=iter(my_list)
print(next(itr))
print(next(itr))
print(next(itr))

#generators
