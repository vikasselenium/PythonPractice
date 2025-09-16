

# reverse a string with string slicing
my_string="Hello World!"
rev_string=[my_string[::-1]]
print(rev_string)

# reverse a string with loop
rev_str=""
for i in range(len(my_string)-1,1,-1):
    #print(my_string[i])
    rev_str=rev_str+" "+my_string[i]
print(rev_string)