'''
File Reading Methods in Python:

There are 4 main methods to read data from a file:
1. read()       – Reads the entire content of the file.
2. read(n)      – Reads the first 'n' characters from the file.
3. readline()   – Reads one line at a time.
4. readlines()  – Reads all lines and returns them as a list.

'''

# f=open('writelines_example.txt','r')
# data=f.read()
# print(data)
# f.close()
#
# with open('writelines_example.txt') as f:
#     data=f.read(5)
#     print(data)


# with open('writelines_example.txt','r') as f:
#     line1= f.readline()
#     print(line1)
#     line2= f.readline()
#     print(line2)

# reading lines with a loop
# with open('writelines_example.txt') as f:
#     line=f.readline()
#     while line!="":
#         print(line,end="")
#         line=f.readline()

# reading lines with readlines() method
with open('writelines_example.txt') as f:
    my_list=f.readlines()
    print("my_list: ", my_list)
    for line in my_list:
        print(line, end="")
