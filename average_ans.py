import sys

sum = 0
count = 0
numbers = []
while True:
    line = ""
    try:
        line = input("enter a number or Enter to finish:")
        if not line:
            break
        numbers.append(int(line))
        count+=1
    except ValueError as err:
        print(err)

numbers.sort()
for x in numbers:
    sum += x

print("count = "+ str(count) + " sum = " + str(sum) + " lowest = " + str(numbers[0]) + " highest = " + str(numbers[-1]) +
      " mean = " + str(sum/count))