
Numbers=[21,56,32,49,87,16,98,5,77]

idx=1
count=len(Numbers)
"""while idx < count:
    for x in range(0, idx):
        if Numbers[idx] < Numbers[x]:
            temp = Numbers.pop(idx)
            Numbers.insert(x, temp)
            break
    idx+=1
print(Numbers)
"""
temp = 0
while idx < count:
    pos=idx
    while pos > 0 and Numbers[pos-1] > Numbers[pos]:
        temp = Numbers[pos-1]
        Numbers[pos-1]=Numbers[pos]
        Numbers[pos]=temp
        pos-=1
    idx+=1
print(Numbers)