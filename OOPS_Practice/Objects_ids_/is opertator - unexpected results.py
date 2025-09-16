

#memory optimization, small integers from -5 to 256

a=257
b=257
print(a is b)
print(id(a))
print(id(b))


a="Hi"
b="Hi"
c="Hi"
d="Hi"
print(a is b)
print(a is b)
print(id(a))
print(id(b))
print(id(c))
print(id(d))