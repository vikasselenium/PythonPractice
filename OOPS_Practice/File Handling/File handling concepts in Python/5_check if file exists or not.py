# os.path.isfile(fname)
# it checks if file exists at given path,used before open() to avoid errors
# if path is not given it looks in current directory

import os

fname=input('Enter file name:')

if os.path.isfile(fname):
    print("file exists==>", fname)
    f=open(fname, 'r')
    data=f.read()
    print(data)
else:
    print("file does not exists!")


