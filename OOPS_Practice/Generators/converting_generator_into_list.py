

def first_n_value_generator(n):
    i=1
    while i<=n:
        yield i
        i=i+1
g=first_n_value_generator(100)
my_list=list(g)
print(my_list)