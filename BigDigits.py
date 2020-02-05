

try:
    row = 0
    numbers = sys.argv[1]
    while row < 5:
        line = ""
        count = 0
        while count < len(numbers):
            number = int(numbers[count])
            digit = digits[number]
            for x in digit[row]:
                if x == "*":
                    line += str(number)
                else:
                    line += " "
            line += " "
            count += 1
        print(line)
        row += 1
except ValueError as err:
    print(err)
except IndexError as err:
    print("usage: BigDigits.py <number>")
