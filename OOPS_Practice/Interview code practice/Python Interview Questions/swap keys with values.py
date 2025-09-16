
'''
d ={'one':1,"two":2, "three":3}, swap keys and values
  o/p- {1: 'one', 2: 'two', 3: 'three'}

'''

d={'one':1,"two":2, "three":3}
swapped={}
for k,v in d.items():
    swapped[v]=k

print(swapped)