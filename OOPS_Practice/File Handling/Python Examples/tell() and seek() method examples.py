'''
Vikas
QA
C#
Selenium

'''

f=open('sample_read.txt', 'r')

print(f.tell())
f.seek(2)
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read())
print(f.tell())
print(f.seek(0))
print(f.tell())
print(f.read())