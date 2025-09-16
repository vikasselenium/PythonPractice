


my_list=[4,5,6,77]

def print_data(alist):
    #print("id of list inside of a function ", id(my_list))
    for item in alist:
        print(item)

#print("id of list outside of a function ", id(my_list))
#print_data(my_list)


your_list=[3,5,6,9]

def multi_list(alist):
    for item in alist:
        item=item*2
        print(item)

multi_list(your_list)
print(your_list)


def multi_list2(alist):
    for i in range(len(alist)):
        alist[i]=alist[i]*2
multi_list2(your_list)
print(your_list)
