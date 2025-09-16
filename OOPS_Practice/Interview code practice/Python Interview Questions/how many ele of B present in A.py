

a=[12,3,4,5,5]
b=[2,3,11,3,111]

cnt=0

for ele in b:
    if ele in a:
        cnt+=1
print(cnt)