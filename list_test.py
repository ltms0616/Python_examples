
Car = "Ford Nissan Mitsubish VW Benz BMW Volvl".split()
print(type(Car))
print(Car)

for i in range(len(Car)):
    print(Car[i])

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x[1::2])
x[1::2]=[0]*len(x[1::2])
print(x)
y = [1]*5
print(y)

leaps = [y for y in range(1900,1940) if (y % 4 == 0 and y % 100 !=0) or (y % 400 ==0)]
print(leaps)

code = [ sex + size + color for sex in "MF" for size in "SMLX" for color in "BGW" if sex != "F" and size != "X"]
code1 = [ sex + size + color for sex in "MF" for size in "SMLX" for color in "BGW" if not (sex == "F" and size == "X")]

code2 = []

for sex in "MF":
    for size in "SMLX":
        if sex == "F" and size == "X":
            continue
        for color in "BGW":
            code2.append(sex+size+color)

print(code)
print(code1)
print(code2)
"""
def product(a, b ,c):
    return a*b*c
num = [2, 3, 5]
result = product(*num)
print(result)"""