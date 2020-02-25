import sys

def lst_find(lst, target):
    idx = 0
    while idx < len(lst):
        if lst[idx] == target:
            break
        idx += 1
    else:
        idx = -1
    return idx

def lst_find1(lst, target):
    for idx in range(len(lst)):
        if lst[idx] == target:
            break;
    else:
        idx = -1
    return idx

def lst_find2(lst, target):
    for idx, x in enumerate(lst):
        if x == target:
            break
    else:
        idx = -1
    return idx

a = "benz"
idx = lst_find2(a, "e")
print(idx)

