
# if we require file to be closed() automatically, even exception occurs
# when control gets out of with statement block, file is closed

with open("contacts.txt", "r") as f:
    data1= f.readline()
    print(data1)
    data2= f.readline()
    print(data2)
    print(f.closed)

print(f.closed)

print("+++++++++++++++++++++++++++++++++++++")
with open("abc.txt", "w") as f:
    f.write("Vikas\n")
    f.writelines(["QA\n","Python\n","Java\n","C#\n"])
    print(f.closed)

print(f.closed)


