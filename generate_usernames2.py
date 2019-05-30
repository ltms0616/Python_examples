import sys
import random
import collections

ID,FOREN,MIDN,SURN,DEP,UNAME = range(6)
User = collections.namedtuple("User", "Id ForeN MidN SurN Dep Uname")
def extract_field(fp):
    users_list={}
    lines = fp.readlines()
    uname_list = set()
    for line in lines:
        data = line.rstrip().split(":")
        uname = "{0}{1}{2}".format(data[3][0], data[2][0], data[1][:5]).lower()
        while uname in uname_list:
            uname += str(random.randint(0,9))
        uname_list.add(uname)
        user=User(data[ID],data[FOREN],data[MIDN],data[SURN],data[DEP], uname)
        users_list[(user.SurN.lower(), user.ForeN.lower(), user.Id)]=user

    return users_list

def main():

    if len(sys.argv) == 1 or sys.argv[1] in ("-h","--help"):
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0]))
        sys.exit()


    users_list = {}
    for filename in sys.argv[1:]:
        fh = open(filename, encoding="utf8")
        users_list = extract_field(fh)
        #print(users_list)

    print("{0:<25} {1:^6} {2:^10}".format("Name", "ID", "Username"))
    print("{0:=<25} {0:=^6} {0:=^10}".format(""))
    for key in sorted(users_list):
        Name="{0}, {1}, {2}".format(users_list[key].SurN, users_list[key].ForeN, users_list[key].MidN[0])
        print("{0:.<25} ({1:>4}) {2:<10}".format(Name, users_list[key].Id, users_list[key].Uname))

main()





