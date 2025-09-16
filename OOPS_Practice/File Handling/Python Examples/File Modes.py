

# text files: text data(.txt)
# binary files: image files(.jpg), audio files(.mp4)

#opening a file - before doing any operation on file we need to open it

#open() -> filename, mode(purpose of opening file)

'''  mode : r(default),    w,     a
            r+             w+     a+    x
'''

f1=open('abc.txt', "r") # "If the file is not found, a FileNotFoundError will be raised."
f2=open('abc_new.txt', "w")
# If the file already contains data, then that data will be overwritten;
# if specified file is not already available, a new file will be created.
f3=open('abc_new.txt', "a")
#it won't overwrite the existing data
#  will be appended, if specified file is not already available, a new file will be created.

# Read and write (r+)
f4=open("abc.txt", "r+")
# read and write
# while writing old will be overwritten

#w+ : Right and Read
# To write and read data
# it will overwrite existing data
# if specified file won't exist, it will create new file

f5=open("abc.txt", "w+")

#a+ : append and read
# to append and read data from the file
#it wont overwrite exisitng data

#x=> exclusive mode for write operation
# x => fileExistsError, if file is available already
# otherwise similar to w



''''

---

### 📁 **File Types**
- **Text files**: `.txt` — store plain text data.
- **Binary files**: `.jpg`, `.mp4` — store images, audio, etc.

---

### 📂 **Opening Files**
Use the `open()` function with:
- **Filename**
- **Mode** — defines the purpose of opening the file.

---

### 🔧 **File Modes**

| Mode | Description |
|------|-------------|
| `r`  | Read-only (default). Raises `FileNotFoundError` if file doesn't exist. |
| `w`  | Write-only. Overwrites existing data or creates a new file if it doesn't exist. |
| `a`  | Append-only. Adds data to the end of the file. Creates a new file if it doesn't exist. |
| `r+` | Read and write. Overwrites existing content while writing. |
| `w+` | Write and read. Overwrites existing data or creates a new file. |
| `a+` | Append and read. Appends data without overwriting. Creates a new file if it doesn't exist. |
| `x`  | Exclusive creation. Raises `FileExistsError` if file already exists. Otherwise, behaves like `w`. |

---

'''


# -----------------------------------------------
# 📁 File Handling in Python - Summary
# -----------------------------------------------

# File Types:
# - Text files: .txt (plain text data)
# - Binary files: .jpg, .mp4 (images, audio, etc.)

# Opening a file:
# Use open(filename, mode) to access a file before performing any operations.

# File Modes:
# 'r'   : Read-only (default). Raises FileNotFoundError if the file doesn't exist.
# 'w'   : Write-only. Overwrites existing data or creates a new file if it doesn't exist.
# 'a'   : Append-only. Adds data to the end of the file. Creates a new file if it doesn't exist.
# 'r+'  : Read and write. Allows reading and writing; writing will overwrite existing content.
# 'w+'  : Write and read. Overwrites existing data or creates a new file.
# 'a+'  : Append and read. Appends data without overwriting. Creates a new file if it doesn't exist.
# 'x'   : Exclusive creation. Raises FileExistsError if the file already exists; otherwise, creates a new file.

# Example usage:
# f1 = open('abc.txt', 'r')    # Read-only
# f2 = open('abc_new.txt', 'w')  # Write-only
# f3 = open('abc_new.txt', 'a')  # Append-only
# f4 = open('abc.txt', 'r+')   # Read and write
# f5 = open('abc.txt', 'w+')   # Write and read
# f6 = open('abc.txt', 'a+')   # Append and read
# f7 = open('abc.txt', 'x')    # Exclusive write

# -----------------------------------------------

# file modes are only for applicable for Text file
# suffix with b, all modes will be then applicable for binary files


# r and r+ => files should be present before operation
# x => file should not be already there if yes fileExists error

# overwriting is going happen
# w, r+, w+

#overwriting not happen: a,a+

