import random

def get_int(msg, min, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            num = int(line)
            if num < min:
                print("must >=", min)
            else:
                return num
        except ValueError as err:
            print(err)

rows = get_int("rows: ", 0, None)
columns = get_int("columns: ", 0, None)
min = get_int("minimum (or Enter for 0): ", -1000,  0)
default = 1000
if default < min:
    default = 2*min
max = get_int("maximum (or Enter for"+str(default)+"): ",min, default)

row = 0
while row < rows:
    col = 0
    line = ""
    while col < columns:
       i = random.randint(min, max)
       s = str(i)
       while len(s)<10:
           s = " "+s
       line += s
       col += 1
    print(line)
    row += 1

