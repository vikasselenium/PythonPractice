'''
program to reverse the string
I/P - "I am writing java program"
o/p - "program java writing am I";
'''

input_string="I am writing java program"

my_list=input_string.split(" ")
rev_string=""
for i in range(len(my_list)-1,-1,-1):
    rev_string =rev_string+ " "+my_list[i]
print(rev_string.strip())