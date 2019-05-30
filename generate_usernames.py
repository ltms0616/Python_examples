import sys
import random
import collections

User = collections.namedtuple("User", "Id ForeN MidN SurN Dep Uname")
def extract_field(fp):
    user_list=[]
    lines = fp.readlines()
    uname_list = []
    for line in lines:
        data = line.strip().split(":")
        uname = "{0}{1}{2}".format(data[3][0], data[2][0], data[1][:5]).lower()
        while uname in uname_list:
            uname += str(random.randint(0,9))
        uname_list.append(uname)
        user_list.append(User(*data, uname))

    return user_list

users_list = {}
fh = open("users.txt", encoding="utf8")
users_list = extract_field(fh)

print("{0:<25} {1:^6} {2:^10}".format("Name", "ID", "Username"))
print("{0:=<25} {0:=^6} {0:=^10}".format(""))
for i in range(len(users_list)):
    Name="{0}, {1}, {2}".format(users_list[i].SurN, users_list[i].ForeN, users_list[i].MidN[0])
    print("{0:.<25} ({1:>4}) {2:<10}".format(Name, users_list[i].Id, users_list[i].Uname))







