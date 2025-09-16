my_string="Hello World"

uniq=[]

for char in my_string:
    if char not in uniq:
        uniq.append(char)

print("".join(uniq))

from datetime import datetime
print(datetime.now().strftime("%d/%m/%Y %I/%M/%D %p"))

#how to import packaage
# first way is directly import package1.package2.module
import OOPS_Practice.Generators.countdown_generator

from OOPS_Practice.Generators import countdown_generator as cg, converting_generator_into_list as cl


my_list=[1,2,3,4]  #Output = [0, 1]

for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i]+my_list[j] ==3:
             print(i,j)
