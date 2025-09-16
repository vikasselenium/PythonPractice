

nums = [5, 1, 4, 2, 3]

length=len(nums)
for i in range(length):
    for j in range(length-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j + 1] =nums[j+1] , nums[j]

print(nums)