
import sys

zero = ["  ***  ", " *   * ", " *   * ", " *   * ", "  ***  "]

one = ["   *   ", "  **   ", "   *   ", "   *   ", "  ***  "]

two = ["  ***  ", " *   * ", "    *  ", "  *    ", " ***** "]

three = ["  ***  ", " *   * ", "   **  ", " *   * ", "  ***  "]

four = ["     * ", "    ** ", "   * * ", "  *****", "     * "]

five = [" ****  ", " *     ", " ****  ", "     * ", " ****  "]

six = ["   *   ", "  *    ", " * * * ", " *   * ", "  ***  "]

seven = [" ***** ", "    *  ", "   *   ", "  *    ", "  *    "]

eight = ["  ***  ", " *   * ", "  ***  ", " *   * ", "  ***  "]

nine = ["  ***  ", " *   * ", "  ***  ", "   *   ", "  *    "]

digits = [zero, one, two, three, four, five, six, seven, eight, nine]

row = 0
count = 0
try:
    numbers = input("Please enter numbers")
    count = len(numbers)
    while x < 5:
        line = ""
        while y < count:
            number = int(numbers[y])
            digit = digits[number]
            line += digit[x]
            y+=1
        x+=1
        print(line)
except ValueError as err:
    print(err)