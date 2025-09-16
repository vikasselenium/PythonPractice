'''

TWO SUM PROBLEM
Input - array = [1,2,3,4] sum = 3
Output = [0, 1]

array = [4,5,7,9] sum = 14
Output = [1, 3]

Fix one index, scan the rest.”
'''

def two_sum(nums, target):
   for i in range(len(nums)):
       for j in range(i+1, len(nums)):
           if nums[i]+nums[j] == target:
               return [i,j]
   return None


print(two_sum([1, 2, 3, 4], 3))    # Output: [0, 1]
print(two_sum([4, 5, 7, 9], 14))   # Output: [1, 3]
