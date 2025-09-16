
def decor_for_division(func):
    def inner(num1,num2):
        if num2==0:
            print("Divider number should not be zero")
            return None
        else:
            return func(num1,num2)
    return inner

@decor_for_division
def division(num1,num2):
    return num1/num2

result=division(10,3)
print(result)