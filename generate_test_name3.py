import sys
import random
import collections

def get_names():
    forenames=[]
    midnames=[]
    surnames=[]

    for names, filenames in ((forenames, "forenames.txt"),
                             (midnames, "midnames.txt"),
                             (surnames, "surnames.txt")):
        for name in open(filenames, encoding="utf8"):
            names.append(name.rstrip())

    return forenames,midnames,surnames

forenames,midnames,surnames = get_names()
id_no= list(range(0,100))
departments=["Admin","Sales","Finance","R&D","Purchasing","QA"]
limit=20
fh = open("users.txt", "w", encoding="utf8")
User = collections.namedtuple("User", "Id Forename Midname Surname Department")
members = []
for id, forename in zip(random.sample(id_no, limit), random.sample(forenames, limit)):
    members.append(User(id, forename, random.choice(midnames), random.choice(surnames), random.choice(departments)))
    members=sorted(members)
for i in range(len(members)):
    fh.write("{0.Id}:{0.Forename}:{0.Midname}:{0.Surname}:{0.Department}\n".format(members[i]))
#    line = "{0}:{1}:{2}:{3}:{4}\n".format(id, forename, random.choice(midnames), surname, random.choice(departments))
#    fh.write(line)

