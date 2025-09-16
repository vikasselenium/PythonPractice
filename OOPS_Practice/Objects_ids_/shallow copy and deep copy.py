
import copy

my_list=(1,[2,4,5],"Vikas")
copied_list=copy.copy(my_list)
print(my_list)
print(copied_list)

copied_list[1][0]="Hello" #list is mutable shared across orginal and copied object
print(my_list)
print(copied_list)

#deep copy
my_list=[12,["vikas",4,55.55],88]
copied_list=copy.deepcopy(my_list)
print("before")
print(my_list)
print(copied_list)

print("after modification")
copied_list[1][0]=66
print("original:",my_list)
print("cloned:",copied_list)