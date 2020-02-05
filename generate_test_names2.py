import sys
import random

if len(sys.argv)<3:
    print("usage: generate_test_names2.py forename_file surname_file")
    sys.exit()
forenames = []
surnames = []
fh = open("test_names2.txt", "w")
for names, file in ((forenames, sys.argv[1]),
                    (surnames, sys.argv[2])):
    for name in open(file):
        names.append(name.rstrip())

limit = 30
years = list(range(1970, 2013))*3
for year, forename, surname in zip(
        random.sample(years, limit),
        random.sample(forenames, limit),
        random.sample(surnames, limit)):
    name = "{0} {1}".format(forename, surname)
    fh.write("{0:.<25}.{1}\n".format(name, year))
