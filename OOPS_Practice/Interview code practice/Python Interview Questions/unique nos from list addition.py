
'''
 write a  program
   i/p - 1,2,3,1,2,0
   output - 6 - (Here only unique numbers get added)
   1+2+3

'''

unique_list=[]
my_list=[1,2,3,1,2,0]

for ele in my_list:
    if ele not in unique_list:
        unique_list.append(ele)

print(sum(unique_list))