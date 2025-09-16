#
# class ReplaceSpace:
#     def __init__(self,input):
#         self.input=input
#
#     def replace_char(self,i):
#         result=""
#         for char in input:
#             if char=="_":
#

my_list=[2,222,3,4,12,3]
#swap method

n=len(my_list)
for i in range(n):
    for j in range(0,n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1] , my_list[j]
print(my_list)

#missing no
'''
Input: nums = [3, 0, 1]
Output: 2

'''
nums = [3, 0, 1]
missing_num=0
for i in range(len(nums)):
    if nums[i]!=i:
        missing_num=i
print(missing_num)

tuple1=(3,0,1) # index, count

#string-> imuumtable data type

my_string="Hello World" #find,index,isupper, islowe
print(my_string.replace("H","K"))

#super() we use for calling parent methods or constructors

