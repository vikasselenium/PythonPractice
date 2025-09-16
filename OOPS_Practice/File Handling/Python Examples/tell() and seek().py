#V i k a s \n
#0 1 2 3 4  5

# it gives current position of file pointer/cursor
with open('abc.txt', 'r') as f:
    print(f.tell())
    print(f.read(2))
    print(f.tell())
    print(f.read(3))
    print(f.tell())
    print(f.read(2))

# seek() -> to move cursor to specific position
# we always seek only from the beginning

#f.seek(3)
