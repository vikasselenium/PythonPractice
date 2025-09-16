
"""
File Handling in Python

Text Files:
    - Contain text data (.txt)

Binary Files:
    - Contain binary data such as images (.jpg), audio/video (.mp4)

Opening a File:
    - Before performing any operation, a file must be opened using the `open()` function.
    - Syntax: open(filename, mode)

File Modes(7):
    'r'   : Read (default) — raises FileNotFoundError if file doesn't exist
    'w'   : Write — overwrites existing data or creates a new file
    'a'   : Append — adds data to the end of the file or creates a new file
    'r+'  : Read and Write — file must exist; allows reading and overwriting
    'w+'  : Write and Read — overwrites all existing data; creates file if not exists
    'a+'  : Append and Read — appends data; does not overwrite existing content
    'x'   : Exclusive creation — raises FileExistsError if file already exists

Examples:

# Read mode
f = open('abc.txt', "r")
Raises FileNotFoundError if file is not found

# Write mode
f = open('abc_new.txt', "w")
# creates a new file if file wont exist or Overwrites existing data

# Append mode
f = open('abc_new.txt', "a")
# Appends data; does not overwrite existing content

# Read and Write (r+)
f = open("abc.txt", "r+")
# Reads and writes; file must exist

# Write and Read (w+)
f = open("abc.txt", "w+")
# Overwrites all data immediately; creates file if not exists

# Append and Read (a+)
f = open("abc.txt", "a+")
# Appends and reads; does not overwrite existing data

# Exclusive creation (x)
f = open("abc.txt", "x")
# Raises FileExistsError if file exists; otherwise behaves like 'w'
"""

# f= open("sample.txt","rb")
# data=f.read()
# print(data)
# f.close()
#

# f= open("sample.txt","w")
# data=f.write("This is a Python code")
# print(data)
# f.close()


# f= open("sample.txt","a")
# f.write("This is an appended line"+" "+"newcontent")
# print("data is appended to the file")
# f.close()

# f=open("sample.txt", 'w+')
# data= f.read()
# print(data)
# f.write("Hello Python")
# print("data is written to the file")

# f=open("sample.txt", 'r+')
# data= f.read()
# print(data)
# f.write("\nthis is another line")
# print("data is written to the file")

# f=open("sample1.txt", 'x')
# f.write("\nExclusive mode")
# print("data is written to the file")

#in order to handle binary files we need to add +b to file modes
'''

Handling  Binary Files in Python:

To work with binary files (like images, audio, etc.), use file modes with 'b':
    - 'rb'  : Read binary
    - 'wb'  : Write binary
    - 'ab'  : Append binary
    - 'r+b' : Read and write binary
    - 'w+b' : Write and read binary
    - 'a+b' : Append and read binary

Adding 'b' to the mode tells Python to treat the file as binary instead of text.

'''