
f=open("sample.txt","r+")

# file object properties
print(f.name)
print(f.mode)
print(f.closed)

print("--------------------")
print(f.readable())
print(f.writable())