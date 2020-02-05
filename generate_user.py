import sys
import random

if len(sys.argv)<4:
    print("usage: generate_user.py forename_file.txt midname_file.txt surname_file.txt")
    sys.exit()

forenames = []
midnames = []
surnames = []
ids = list(range(1, 1000))
departments=["Sales", "R&D", "Admin", "HR", "Account", "Marketing"]
fh = open("user.txt", "w")
for names, file in ((forenames, sys.argv[1]),
              (midnames, sys.argv[2]),
              (surnames, sys.argv[3])):
    for name in open(file):
        names.append(name.rstrip())

limit=50
id_n = random.sample(ids, 50)
for i in range(limit):
    midname = random.choice(midnames)
    line = "{0}:{1}:{2}:{3}:{4}".format(id_n[i],
                                        random.choice(forenames),
                                        random.choice((midname,"")),
                                        random.choice(surnames),
                                        random.choice(departments))

    fh.write(line+"\n")
fh.close()