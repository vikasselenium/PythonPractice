
'''
Write the program for the print list in ascending order

'''

my_list=[2.4,222,3,4,12,3]
print(sorted(my_list))

# swap method
n=len(my_list)
for i in range(n):
    for j in range(0,n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] =  my_list[j+1],  my_list[j]

print(my_list)

'''
# for visualize 
my_list = [2.4, 222, 3, 4, 12, 3]

n = len(my_list)
step = 1
for i in range(n):
    print(f"\nPass {i+1}:")
    for j in range(0, n - i - 1):
        a, b = my_list[j], my_list[j + 1]
        print(f"  Step {step:02d} – compare (idx {j},{j+1}): {a} > {b}? ", end="")
        if a > b:
            print("Yes → swap")
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        else:
            print("No  → no swap")
        print("     ", my_list)
        step += 1

print("\nSorted:", my_list)





'''