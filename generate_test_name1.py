import sys
import random

def get_forename_and_surname():
    forenames=[]
    surnames=[]

    for names, filenames in ((forenames, "forenames.txt"),
                             (surnames, "surnames.txt")):
        for name in open(filenames, encoding="utf8"):
            names.append(name.rstrip())
    return forenames,surnames

forenames,surnames = get_forename_and_surname()
fh = open("name_list.txt", "w", encoding="utf8")
for i in range(10):
    line = "{0}:{1} {2}\n".format(i, random.choice(forenames), random.choice(surnames))
    fh.write(line)