

a = [2,3,4,5]
b = [2,3,4,5]

print(a is b)

a1=15
b1=15

print(a1 is b1)

a2=(1,2,3)
b2=(1,2,3)
print(a2 is b2)

set1={1,2,3}
set2={1,2,3}
print(set1 is set2)


fset1 = frozenset([1, 2, 3])
fset2 = frozenset([1, 2, 3])
print(fset1 is fset2)

# is --> checks the Objects/refrences
# == --> check the values

print("++++++++++")
a=[1,2,3,4]
b=[1,2,3,4]
print(a is b)
print(a == b)