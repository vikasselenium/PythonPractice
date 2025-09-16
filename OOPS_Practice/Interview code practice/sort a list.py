
#Write program to sort list of integer element (Done with 2 for loop).

my_list=[3,5,6,2,4,5]

for i  in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] >  my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)