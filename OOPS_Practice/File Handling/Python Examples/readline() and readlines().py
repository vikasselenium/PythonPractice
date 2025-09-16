

# f=open('contacts.txt','r')
# line1=f.readline()
# print(line1) # print will add \n and line  also have \n, so one extra line
# line2=f.readline()
# print(line2)
# f.close()

# if there are large no of lines
# readline() returns empty string when it reaches to EOF
f=open('contacts.txt', 'r')
line=f.readline()
while line != "":
    print(line, end='')
    line=f.readline()
f.close()

print("\n+++++++++++++++++++++++++")
f=open('abc.txt', 'r')
my_list=f.readlines()
print(my_list)
for line in my_list:
    print(line,end='')

