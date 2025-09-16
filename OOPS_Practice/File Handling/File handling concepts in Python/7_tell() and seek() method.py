'''
Vikas
QA
JAVA
C#
Selenium
'''


with open('tell_seek_example.txt','r') as f:
    print(f.tell()) # it will give current location of file cursor
    print(f.read(2))
    print(f.tell())

    print(f.seek(0)) # beginning of file
    print(f.tell())