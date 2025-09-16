
def my_gen():
    yield "A"
    yield "B"
    yield "C"

g=my_gen()
# print(type(g))
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # here we will get StopIteration

# in order to avoid StopIteration exception, use a for loop

for i in g:
    print(i)