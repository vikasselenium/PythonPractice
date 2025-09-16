# example for try and except block
errors=[]

try:
    # a=5
    # b=0
    # c=a/b
    f=open("abc.txt","r+")
    data= f.read()
    print(data)

except ZeroDivisionError as e:
    print("Exception occurred==>", e)

except Exception as e:
    print(e)

else:
    print("Exception not occurred hence -Else part")

finally:
    print("statement in finally block executes always")
    f.close()