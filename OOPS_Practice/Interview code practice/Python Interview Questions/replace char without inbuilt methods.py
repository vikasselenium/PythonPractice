'''

Given string replace the space to variable and use class,
variable method and   object. Do not used any inbuilt method.
input = "h_ are you do_ng today"
variable = "i"

'''

class ReplaceSpace:
    def __init__(self,input_string):
        self.input_string=input_string

    def replace_char(self,i):
        res_string=""
        for char in self.input_string:
            if char == '_':
                res_string=res_string+i
            else:
                res_string=res_string+char
        return res_string

re_char=ReplaceSpace("h_ are you do_ng today")
print(re_char)