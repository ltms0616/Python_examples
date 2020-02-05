
names = ["Blair", "Riley", "Ben", "John", "Josh", "Murray", "Sam", "Grayson"]
print(sorted(names, key=str.lower))

def swap(t):
    return t[1], t[0]
x = list(zip((1, 3, 1, 3), ("pram", "dorie", "kayak", "canoe")))
print(x)
print(sorted(x))
print(sorted(x, key=swap))