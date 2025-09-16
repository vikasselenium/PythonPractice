
'''
Input: nums = [3, 0, 1]
Output: 2

Input: nums = [0, 1]
Output: 2

'''

nums=[3,0,1]
#nums=[0, 1]

nums.sort()
print(nums)
missing_num=0

i=0
for i in range(len(nums)):

   if nums[i] != i:
       missing_num=i
       break
   else:
       missing_num=i+1

print(missing_num)