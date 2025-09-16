# there are 4 methods available for reading character data from a file

# read() --> to read total data from the file
# read(n) --> to read 'n' characters from the file
# readline() --> to read only one line
# readlines() --> to read all lines into a list

# f=open('abc.txt','r')
# data=f.read()
# print(data)
# f.close()

f=open('abc.txt', 'r')
#data=f.read(7) #7 characters
data=f.read(-1) #total characters
print(data)
f.close()