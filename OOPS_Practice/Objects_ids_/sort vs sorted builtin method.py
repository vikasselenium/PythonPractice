
my_list=[6,2,7,1]
my_list.sort() # this is  in place operation, it will sort values..it will mutate
print(my_list)

# use sorted method without mutating original object
my_list=[6,2,7,1]
print(sorted(my_list))# without mutating original list
print(my_list)

# we should not use a list as default argument
