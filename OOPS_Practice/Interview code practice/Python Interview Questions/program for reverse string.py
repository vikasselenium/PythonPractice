
my_string="Hello World!"
rev_string=""
for i in range(len(my_string)-1,-1,-1):
    rev_string=rev_string+my_string[i]

print(rev_string)

print(my_string[::-1])