a=[12,3,4,5,5]
b=[2,3,11,3,111,12]

set1=set(a)
set2=set(b)

print(set1.intersection(set2))

cnt=0
rem_dup=[]


for ele in b:
    if a.count(ele)>=1 and ele not in rem_dup:
        cnt=cnt+1
        rem_dup.append(ele)
print(cnt)

# r = "abcabdcbb", find the longest substring in which no characters are repeated.
r = "abcabdcbb"
longest=""
for i in range(len(r)):
    current=""
    for j in range(i,len(r)):
        if r[j] in current:
            break
        else:
            current=current+r[j]

#9.	d ={'one':1,"two":2, "three":3}, swap keys and values
#  o/p- {1: 'one', 2: 'two', 3: 'three'}

d ={'one':1,"two":2, "three":3}
swapped={}
for k,v in d.items():
    swapped[v]=k
print(swapped)

set11= {1, 4, 3, 7, 5, 8, 2, 9}
my_list=list(set11)
my_list.sort(reverse=True)
print(my_list)
print(my_list[1])

input_string="I am writing java program"

