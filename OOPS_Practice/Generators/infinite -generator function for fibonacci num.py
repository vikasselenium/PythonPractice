
# 0,1, 1, 2 , 3...
# a b


def generate_fib_numbers():
    a, b=0,1
    while True:
        yield a
        a,b= b,a+b

g=generate_fib_numbers()
for i in g:
    print(i)

