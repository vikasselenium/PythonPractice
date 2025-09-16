
nums = [5, 1, 4, 2, 3]

sorted_nums=[]

while nums:
    m=min(nums)
    nums.remove(m)
    sorted_nums.append(m)

print(sorted_nums)