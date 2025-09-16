def creating_gen(index):
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    yield months[index]
    yield months[index+2]

next_month = creating_gen(3)
print(next(next_month), next(next_month))

# threading module we can use..thread.start(task1) and task2 and then join

a={"x":1,"y":2}
b={"y":3,"z":4}

c=a|b
print(c)

#sorting a dict
d = {"b": 2, "a": 3, "c": 1}
# print("++++++++++sorting..in dict by key +++++++++++")
# for k in sorted(d.keys()):
#     print(k, d[k])
# print("++++++++++sorting..in dict by value +++++++++++")
# d = {"b": 2, "a": 3, "c": 1}


#sorting by keys
for k in sorted(d.keys()):
    print(k,d[k])

def get_value(item):
    print(item)
    return item[1]

#sorting dict by values
for k,v in sorted(d.items(),key=get_value):
    print(k,v)