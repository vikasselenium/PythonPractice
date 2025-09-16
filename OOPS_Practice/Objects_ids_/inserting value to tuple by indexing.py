

a=(1,2,3,4)
print(id(a))
a=a[:2]+(7,)+a[2:]
print(id(a))
print(a)