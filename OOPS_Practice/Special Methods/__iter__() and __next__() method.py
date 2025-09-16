# my_list = [2, 3, 4, 5]
#
# for elem in my_list:
#     print(elem)

#The __iter__() and __next__() methods work together to create this amazing functionality in our for loops

#First, the __iter__() method returns an iterator object from the iterable.

#Once we have that iterator, the special method __next__() can be called to get the next element in the iterator until all the elements have been used.


my_list = [2, 3, 4, 5]
iterator = my_list.__iter__()
print(iterator)
print(type(iterator))
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
#print(iterator.__next__())
#print(iterator.__next__())

print("####################")
iterator=iter(my_list)
for ele in iterator:
    print(ele)

#The special method __iter__() returns an iterator object from the
# iterable and the special method __next__() returns the next element in the iterator.