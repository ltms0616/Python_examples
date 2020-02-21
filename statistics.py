import sys
import collections
import math

Statistics = collections.namedtuple("Statistics", "mean mode median std_dev")

def print_result(count, stat):
    real = "9.2f"
    if stat.mode == None:
        modeline = ""
    elif len(stat.mode) == 1:
        modeline = "mode      = {0:{fmt}}\n".format(stat.mode[0], fmt = real)
    else:
        modeline = "mode     = [" + ", ".join(["{0:.2f}".format(m) for m in stat.mode]) + "]\n"
    print("""
    count     = {0:6}
    mean      = {mean:{fmt}}
    median    = {median:{fmt}}
    {1}\
    std. dev. = {std_dev:{fmt}}""".format(count, modeline, fmt=real, **stat._asdict()))

def calculate_std_dev(numbers, mean):
    total = 0
    for number in numbers:
        total += ((number -mean)**2)
    variance = total / (len(numbers)-1)
    return math.sqrt(variance)

def calculate_median(numbers):
    numbers = sorted(numbers)
    middle = len(numbers)//2
    median = numbers[middle]
    if  len(numbers)%2 == 0:
        median = (median + number[middle-1])/2
    return median

def calculate_mode(frequencies, maximum_modes):
    high_freq = max(frequencies.values())
    mode = [number for number, freq in frequencies.items() if freq == high_freq]
    if not (1 <= len(mode) <= maximum_modes):
        mode = None
    else:
        mode.sort()
    return mode

def calculate_statistics(numbers, frequencies):
    mean = sum(numbers)/len(numbers)
    mode = calculate_mode(frequencies, 3)
    median = calculate_median(numbers)
    std_dev = calculate_std_dev(numbers, mean)
    return Statistics(mean,mode,median, std_dev)

def read_data(numbers, file, frequencies):
    for lino, line in enumerate(open(file, encoding="ascii"), start=1):
        for x in line.split(" "):
            try:
                number = float(x)
                numbers.append(number)
                frequencies[number] +=1
            except ValueError:
                print("{file}:{lino}: skipping {x}: {err}".format(**locals()))

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: statistics.py [data file1] [data file2] ...")
        sys.exit()

    frequencies = collections.defaultdict(int)
    numbers = []
    for file in sys.argv[1:]:
        read_data(numbers, file, frequencies)
    if numbers:
        stat = calculate_statistics(numbers, frequencies)
        print_result(len(numbers), stat)
    else:
        print("no member found")

main()