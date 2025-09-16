

def generate_fib_series():
    a,b =0,1
    while True:
        yield a
        a,b=b,a+b

g=generate_fib_series()
for i in g:
    # if I want to print fib series till 100
    if i <=1000:
        print(i)
    else:
        break


