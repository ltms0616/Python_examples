import sys

lowest = None
highest = None
nums=[]
total = 0
while True:
    try:
        line = input("enter a number or Enter to finish:")
        if not line:
            break
        num = int(line)
        if lowest is None or lowest > num:
            lowest = num
        if highest is None or highest < num:
            highest = num
        total += num
        nums.append(num)
    except ValueError as err:
        print(err)

print("numbers=",nums)
count = len(nums)
print("count=",count,"total=", total, "mean=", total/count,  "min=", lowest, "max=", highest)
