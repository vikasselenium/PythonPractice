
# various properties of the object
f=open("abc.txt", "x")
print('File Name:',f.name)
print('File Mode:',f.mode)
print('Is File Closed:',f.closed)

print('Is file Readable:',f.readable())
print('Is file Writable:',f.writable())

f.close()
print('Is File Closed:',f.closed)