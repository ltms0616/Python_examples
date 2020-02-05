import sys
import collections

User = collections.namedtuple("User", "username forename midname surname id")
ID, FORENAME, MIDNAME, SURNAME, DEPARTMENT = range(5)

def generate_username(field, usernames):
    username = field[FORENAME][0]+field[MIDNAME][:1]+field[SURNAME]
    username = original = username[:8].lower()
    count = 1
    while username in usernames:
        username = original+str(count)
        count += 1
    usernames.add(username)
    return username
def process_line(line, usernames):
    field = line.rstrip().split(":")
    username=generate_username(field, usernames)
    user = User(username, field[FORENAME], field[MIDNAME], field[SURNAME], field[ID])
    return user

def print_users(users):
    namewidth=32
    unamewidth=10
    print("{0:<{nw}}{1:^6}{2:^{uw}}".format("NAME", "ID", "username", nw=namewidth, uw=unamewidth))
    print("{0:-<{nw}}{0:-^6}{0:-^{uw}}".format("", nw=namewidth, uw=unamewidth))
    for key in sorted(users):
        user = users[key]
        mid = ""
        if user.midname:
            mid = " " + user.midname[0:1]
        name = "{0.surname}, {0.forename}{1}".format(user, mid)
        print("{0:.<{nw}} {1:^6} {2:<{uw}}".format(name, user.id, user.username, nw=namewidth, uw=unamewidth))

if len(sys.argv)<2:
    print("usage: generate_username.py user.txt")
    sys.exit()

usernames = set()
users = {}
for line in open(sys.argv[1]):
    user=process_line(line, usernames)
    users[(user.surname.lower(), user.forename.lower(), user.id)] = user

print_users(users)