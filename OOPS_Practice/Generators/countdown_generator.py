
import time
def countdown_generator(n):
    while n >= 0:
        yield n
        n=n-1

g=countdown_generator(5)
for i in g:
    time.sleep(1)
    print(i)