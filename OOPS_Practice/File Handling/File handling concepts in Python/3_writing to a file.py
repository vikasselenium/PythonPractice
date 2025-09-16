# there are 2 methods available for writing characters to a file.
# f.write(str)
# f.writelines(list of strings)
# with statement

# with open("write_example.txt", "w") as f:
#     f.write("Hello, Python!")
#     f.write("\nHello, World!")
#     print(f.closed)
# print(f.closed)

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("writelines_example.txt", "w") as f:
    f.writelines(lines)
    print("Lines written using writelines()")
