

i = iter([1, 2,4, 8])
print(type(i))
while True:
    try:
        print(next(i))
    except StopIteration:
        break