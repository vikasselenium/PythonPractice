
a=[2,3,4,5,6]
b=a[:] # here we are cloning a list
a[0]=15
print(a)
print(b)

org=[1,3,4,5,6]
cloned=org.copy()
cloned[0]=20
print(org)
print(cloned)