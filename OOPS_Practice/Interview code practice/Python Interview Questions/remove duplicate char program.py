
my_string="Hello World"

unique_chars=[]

for char in my_string:
    if char not in unique_chars:
        unique_chars.append(char)

res="".join(unique_chars)
print(res)
