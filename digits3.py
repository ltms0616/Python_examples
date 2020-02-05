import sys

Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column  = 0
        while column < len(digits):
            num = int(digits[column])
            Digit = Digits[num]
            for i in Digit[row]:
                if i == "*":
                    i = str(num)
                line += i
            line += " "
            column += 1
        row += 1
        print(line)
except IndexError:
    print("Usage: digits2.py <number>")
except ValueError as err:
    print(err, "in", digits)