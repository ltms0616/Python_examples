import sys

Margin = False

if Margin is True:
    offset1 = 100 + 10
else:
    offset1 = 100
print(offset1)

offset = 100 + (10 if Margin is True else 0)
print(offset)

count = 1

print("{0} file{1}".format(count if count != 0 else "no", "s" if count != 1 else ""))