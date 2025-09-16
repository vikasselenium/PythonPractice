

def first_n_values_generator(n):
    i=1
    while i<=n:
        yield i
        i+=1

g= first_n_values_generator(100) # we get generator object here
for i in g:
    print(i)
