
fname=input("Enter a file name: ")
f=open(f"{fname}.txt","w")

while True:
    data=input("Enter data to add file: ")
    f.write(data+"\n")
    option=input("Do you want to add text again[Yes/No]: ")
    if option.lower()=="no":
        break
print("Data written to the file successfully")
f.close()