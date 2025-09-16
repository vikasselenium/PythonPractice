


set1={13,23,1,4,5,6,6,7,8,11}
print(set1)

# set is an un-ordered collection
# it doesn't contain duplicate values
# indexing and slicing is not supported
# insertion order is not maintained


#methods: add(), remove()
#Empty set
set2=set()
print(type(set2))

#set with some values
set3=set([1,3,4,5,6,6,6,2])
print(set3)

# add(x) vs update(iterable)
set3.add(222)
print(set3)
set3.update([333,444]) # update does union with any iterable
print(set3)

#remove(x) vs discard(x) vs pop()
#set3={1, 2, 3, 4, 5, 6, 333, 444, 222}
set3.remove(444)
print(set3)

# remove if ele doesn't exist
#set3.remove(444) #KeyError
print(set3)

set3.discard(444) # no error if 444 is not present
print(set3)

popped_item=set3.pop()
print(popped_item)
print(set3)


#Algebra:
s={1,2,3,4}
t={2,4,5}
t1={1,2}
t3={11,22}

#union
print(s|t) #s.union(t); {1, 2, 3, 4, 5}
print(s&t) #s.intersection(t); {2, 4}
print(s-t) #s.difference(t);{1, 3}


# relations
print(t1.issubset(s))
print(s.issuperset(t1))
print(s.isdisjoint(t3))

