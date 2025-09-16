

try:
    a=11
    b=0
    c=a/b

    f=open("ddfdf.txt","r")
    data= f.read()

except ZeroDivisionError as e:
    print("Exception 1::", e)


