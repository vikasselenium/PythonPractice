

def gen_fib_series():
    a,b =0,1
    while True:
        yield a
        a,b = b, a+b

#getting generator object
g=gen_fib_series()
count=1
for i in g:
    if count <=10:
        print(i, end=' ')
        count=count+1
    else:
        break
