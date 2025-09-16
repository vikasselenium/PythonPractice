
def find_second_max_num_in_list(my_list):
    t_set=set(my_list)
    t_list= list(t_set)
    t_list.sort(reverse=True)
    return t_list[1]

my_list=[12,3,4,111,3,4,55,77,77,88,88, 111]
print(find_second_max_num_in_list(my_list))

print(type(find_second_max_num_in_list))