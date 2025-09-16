
# for writing character data to file, two Methods are available:
#  f.write(str)
#  f.writelines(list of strings)

f=open("abc.txt", "w")
f.write("Vikas")
f.write("QA")
f.write("Pune")
f.close()
print("Data written to the file successfully")

f=open("abc_new.txt", "w")
names = ["Amit", "Vikas", "Rahul", "Aryan"]
#d={"Amit":"one","Vikas":"two","Rahul":"three","Aryan":"four"}
# f.writelines(d)
#f.writelines(d.values())
f.writelines(names)
print("Data written to the file successfully")
f.close()

# instead of list we can pass tuple and set
# in case of set order will not be preserved
# if we pass dictionary only keys would be added, however keys should be string type only

