
#[1,2,3,3,4,5,6,7] => [3,6,9,13]

my_list=[1,2,3,3,4,5,6,7]

for i in range(0,len(my_list)-1,2):
    print(my_list[i]+my_list[i+1])
