
Numbers=[21,56,32,49,87,16,98,5,77]
print("Before sort"+str(Numbers))
min_idx = 0
count = len(Numbers)
min = 0
idx = 0

while idx < count:
    min_idx=idx
    for x in range(idx+1, count):
        if Numbers[min_idx] > Numbers[x]:
            min_idx = x
    #min = Numbers[min_idx]
    #Numbers[min_idx]=Numbers[idx]
    #Numbers[idx]=min
    Numbers[min_idx], Numbers[idx]=Numbers[idx], Numbers[min_idx]
    idx+=1
print("after Sort"+str(Numbers))


