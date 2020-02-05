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

digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

def print_digits(msg):
    for i in range(7):
        line = ""
        for number in msg:
            try:
                num=int(number)
                Digit = digits[num]
                line += Digit[i] + " "
            except ValueError as err:
                print(err)
        print(line)

if len(sys.argv) < 2:
    print("Usage: digits.py <numbers>")
else:
    print_digits(sys.argv[1])