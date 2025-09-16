
#r = "abcabdcbb", find the longest substring in which no characters are repeated.
#🔥 Memory Trick:
#“Start at each index, grow until repeat, keep the longest.”

r="abcabdcbb"

longest=""

for i in range(len(r)):
    current=""
    for j in range(i,len(r)):
        if r[j] in current:
            break
        else:
            current=current+r[j]
    if len(current) > len(longest):
        longest =current

print(longest)