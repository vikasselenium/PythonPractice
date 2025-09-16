

def my_generator(n):
    for i in range(n):
        yield i

gen=my_generator(5) # it returns generator object
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

print("#######################")
for item in gen:
    print(item)