import random
import sys

if len(sys.argv)<3:
    print("usage: generate_test_names.py [forename file] [surname file]")
    sys.exit()

forename=[]
surname=[]
fore_file = sys.argv[1]
sur_file = sys.argv[2]
test_name_file = open("test_name.txt", "w")
for names, filename in ((forename, sys.argv[1]),
                        (surname, sys.argv[2])):
    for name in open(filename, encoding="utf8"):
        names.append(name.rstrip())

for i in range(100):
    line = "{0} {1}\n".format(random.choice(forename), random.choice(surname))
    test_name_file.write(line)
