import sys

if len(sys.argv)<3:
    print("usage: grepword [word] [file1] ....")
    sys.exit()

word = sys.argv[1]
for filename in sys.argv[2:]:
    try:
        for lino, line in enumerate(open(filename), start=1):
            if word in line.lower():
                print("{0}:{1}:{2}".format(filename, lino, line.rstrip()))
    except FileNotFoundError:
        break
