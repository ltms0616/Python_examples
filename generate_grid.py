import sys
import random

def get_input_data(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            num = int(line)
            if num < minimum:
                print("the number must >"+minimum)
            else:
                return num
        except ValueError as err:
            print(err)

rows = get_input_data("rows:", 1, None)
cols = get_input_data("cols:", 1, None)
minimum = get_input_data("minimum(or Enter for 0):", -1000, 0)
def_max = 1000
if minimum > def_max:
    def_max = 2*minimum
maximum = get_input_data("maximum(or Enter for"+str(def_max)+"):", minimum, def_max)

row = 0
while row < rows:
    line = ""
    col = 0
    while col < cols:
        number = random.randint(minimum, maximum)
        s = str(number)
        while len(s) < 10:
            s = " "+s
        line += s
        col += 1
    print(line)
    row += 1



