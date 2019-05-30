
"""
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(10))
"""

table = [0]*3
table[0] = 0
table[1] = 1

for x in range(2, 11):
    table[2] = table[0]+table[1]
    table[0] = table[1]
    table[1] = table[2]

print(table[2])