'''
Given string replace the space to variable and use class,
variable method and   object. Do not used any inbuilt method.
input = "h_ are you do_ng today"
variable = "i"

'''

class ReplaceSpace:
    def __init__(self, input_str):
        self.input_str=input_str

    def replace_space_with_char(self,i):
        words=self.input_str.split(" ")
        res_str=""
        for word in words:
            new_word = ""
            for char in word:
                if char == "_":
                    new_word=new_word+i
                else:
                    new_word=new_word+char

            res_str=res_str+ new_word +" "
        #print(res_str)
        return res_str

input_str=ReplaceSpace("h_ are you do_ng today")
print(input_str.replace_space_with_char("i"))