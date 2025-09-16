#Input:  "aaabbbcccc"
# Output: {'a': 3, 'b': 3, 'c': 4}

my_string="aaabbbcccc"
my_dict=dict()

#using dict
for char in my_string:
    if char in my_dict:
        my_dict[char] = my_dict[char]+1
    else:
        my_dict[char]=1
print(my_dict)
