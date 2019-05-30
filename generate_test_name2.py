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
limit=10
years = list(range(1970,2013))
fh = open("name_list.txt", "w", encoding="utf8")
for year, forename, surname in zip(random.sample(years, limit), random.sample(forenames, limit),
                                   random.sample(surnames, limit)):
    name = "{0} {1}".format(forename, surname)
    fh.write("{0:.<25}.{1}\n".format(name, year))