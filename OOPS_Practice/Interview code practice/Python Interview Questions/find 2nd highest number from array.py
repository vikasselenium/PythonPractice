'''
Write a program to find 2nd highest number from array;
 I/P - {1,4,3,7,5,8,2,9}
 o/p – 8

'''

input_array= {1,4,3,7,5,8,2,9}

my_list=list(input_array)
my_list.sort(reverse=True)
print(my_list[1])

# alternatie way
# sorting an array

n=len(my_list)
for i in range(n):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j],my_list[j+1] = my_list[j+1], my_list[j]
print(my_list[-2])