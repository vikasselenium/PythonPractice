

# dictionary contains key-value pairs

d={"one":1, "two":2, "three":3}

#create a empty dict
d1={}
print(type(d1))

d2=dict()
print(type(d2))

#Can dictionary keys be mutable?
d1={(1,2), "ok"}
#d2={[1,2],"Not Ok"} # gives TypeError
print(d1)

#d={"one":1, "two":2, "three":3}
# Check if a key exists?
print(d.get('two')) #returns value if key is present
print(d.get("Hundred")) # returns None value if key is not present

# Access, Update & Defaults
# dict.get() vs d[key]?
print(d['two']) # returns value if key exists
#print(d["Hundred"]) # KeyError if key is missing
print(d.get('twow',0)) # we can also return any value if key is missing

#update or insert?
d['hundred'] =100 # adding value to dict
d["two"] =22 #update value for key "two"
print(d)

#Merge Dictionaries
a={"x":1,"y":2}
b={"y":3,"z":4}

c=a|b
print(c) #{'x': 1, 'y': 3, 'z': 4}

#Remove items
print("###############################################")
#{'one': 1, 'two': 22, 'three': 3, 'hundred': 100}
print(d)
print(d.popitem()) # removes LAST inserted (LIFO)
print(d)
print(d.pop("two",-1))
print(d)
print(d.pop("two",-1))
# delete item from dictionary
del d["one"]
print(d)
# del d["one"]  # KeyError if key is missing

d.clear() # remove all items
print(d)

#What are keys(), values(), items()?
d= {'x': 1, 'y': 3, 'z': 4}

for k in d.keys():
    print(k)

for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k,v)

# sorting dictionary
# sorting by a key
d = {"b": 2, "a": 3, "c": 1}
print("++++++++++sorting..in dict by key +++++++++++")
for k in sorted(d.keys()):
    print(k, d[k])
print("++++++++++sorting..in dict by value +++++++++++")
d = {"b": 2, "a": 3, "c": 1}
def get_value(item):
    return item[1]

for k,v in sorted(d.items(),key=get_value):
    print(k,v)

# count each character in string
my_string='banana'
my_dict={}
for ch in my_string:
    if ch in my_dict.keys():
        my_dict[ch]=my_dict[ch]+1
    else:
        my_dict[ch]=1
print(my_dict)