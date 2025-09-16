# text files: text data(.txt)
# binary files: image files(.jpg), audio files(.mp4)

# opening a file - before doing any operation on the files we need to open it

# open() -> filename, mode(purpose of opening file)

'''  mode : r(default),    w,     a
            r+             w+     a+    x
'''

#read mode
#f=open('abc.txt', "r") # "If the file is not found, a FileNotFoundError will be raised."

#write mode
# f=open('abc_new.txt', "w")
# If the file already contains data, then that data will be overwritten;
# if specified file is not already available, a new file will be created.

#append mode
#  f=open('abc_new.txt', "a")
#  it won't overwrite the existing data
#  data will be appended / a new file will be created if file does not exists

# Read and write (r+)
# f=open("abc.txt", "r+")
# read and write
# Keeps existing content; you can read and overwrite parts of it.
# FileNotFoundError if file doesn't exist

#  write and Read (w+)
# To write and read data
# it will overwrite all existing data immediately
# Creates file if not exists: No error if the file doesn't exist.

# f5=open("abc.txt", "w+")

#a+ : append and read
# to append and read data from the file
# it won't overwrite existing data

#x=> exclusive mode for write operation
# x => fileExistsError, if file is available already
# otherwise similar to 'w' mode
