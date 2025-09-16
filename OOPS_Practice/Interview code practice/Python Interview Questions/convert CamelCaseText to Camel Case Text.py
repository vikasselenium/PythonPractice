'''

13.	write a program to convert "CamelCaseText" to "Camel Case Text",
    use class, variable method and object,
    do not used any inbuilt method.’

'''

class CamelCaseText:
    def __init__(self,str):
        self.str=str

    def converter(self):
        result=""
        for char in self.str:
            if char.isupper():
                result=result+" "

            result=result+char
        return result.strip()

con = CamelCaseText("CamelCaseText")
print(con.converter())



