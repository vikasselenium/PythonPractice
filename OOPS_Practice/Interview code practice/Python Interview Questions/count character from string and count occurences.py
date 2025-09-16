'''
to count the character in the string
str = "aaabbbcccc" and output like a:3, b:3, c:4

'''

my_str="aaabbbcccc"
my_dict={}

for char in my_str:
    if char in my_dict:
        my_dict[char] = my_dict[char]+1
    else:
        my_dict[char] = 1

print(my_dict)