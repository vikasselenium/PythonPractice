#generator are special function that uses yield keyword instead of return
#it yields one value at a time

def my_gen():
    print("inside generator function")
    yield "A"
    yield "B"
    yield "c"

g=my_gen()

itr=iter(g)
print(next(itr))
print(next(itr))

# for i in g:
#     print(i)

# 0 1 1 2 3 5 ...

def gen_fib(num):
    a,b= 0,1
    cnt=0
    while True:
        if cnt < num:
            a,b=b,(a+b)
            print(a, end=' ')
            cnt=cnt+1
        else:
            break
gen_fib(15)
