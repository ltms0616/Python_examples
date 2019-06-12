


""""#order of functions
def main():
    sqcode()

def sqcode():
    sq_code = ord("\N{SUPERSCRIPT TWO}")
    print(sq_code)
    print(chr(sq_code))

main()
"""

"""# Read lines from file
#case 1
fp = open("country_data.txt", "r")
#for line in iter(fp):
for line in fp:
    print(line)
fp.close()
"""

#case 2
"""fp = open("country_data.txt", "r")
line = fp.readline()
print(type(line))

while line:
    print(line)
    line=fp.readline()
fp.close()"""


#case 3
"""with open("country_data.txt", "r") as fp:
    all_lines = fp.readlines()
    print(type(all_lines))

for line in all_lines:
    print(type(line))
    print(line)"""

#Read line from file and append into list
"""def read_lines(fp):
    line=fp.readline()
    print(type(line))
    print(line)
    quote = None
    field = ""
    fields = []
    while line:
        for x in line:
            if x in "\"'":
                if quote is None:
                    quote = x
                elif quote == x:
                    quote = None
                else:
                    field += x
            elif x == ",":
                fields.append(field)
                field = ""
            else:
                field += x
        line = None
        #line = fp.readline()
    fields.append(field)
    return fields



    #for line in lines:
    #print(lines)

fp = open("country_data.txt", "r")
fields=read_lines(fp)
print(fields)
fp.close()"""

# Test the argv
"""import sys

word = ""
words = []
if len(sys.argv)>1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: test.py [option] [word]")
    else:
        print("count of argv is {0}".format(len(sys.argv)))
        for x in range(len(sys.argv)):
            word = sys.argv[x].lower()
            words.append(word)
        print(words)

if not words or words[1] in ("-a", "--all"):
    print("print all table")
else:
    print("print word")"""

#Test word in string
"""test = ["test", "ko"]
result = "test is ko"
tmp_result=[]
flag = 0
for x in test:
    if x in result:
       print("{} inside".format(x))
       flag+=1
if flag == len(test):
    print(result)
"""

#test enumerate
"""for i in enumerate(("aoki", "nami", "riko"), start=1):
    print(i)"""

#test unpack
"""def calculate(a,b,c,d):
    sum=a+b+c+d
    print(sum)
t = (5,12,15,9)
calculate(*t)
calculate(*range(1,5))"""

#test path separate symbol change regard to OS
"""import os
test_path = "C:/test/audio"
print(test_path.replace("/", os.sep))"""

#test random sample
"""import random
limit = 5
years = list(range(1970,2013))*3
print(years)
sample_years = random.sample(years, limit)
print(sample_years)"""

#test zip
"""x = []
for t in zip(range(-10,0,1), range(0,10,1), range(1,10,2)):
    x+=t
print(x)

t = (2,3,4)
s = (5,6,7)
x+=t
print(x)
x+=s
print(x)
t+=s
print(t)"""


#test isalnum
"""line = "fdsdaf http://tw.yahoo.com.php  ==>"
idx = 0
idx = line.find("http://", idx)
if idx != -1:
    site=None
    idx += len("http://")
    for j in range(idx, len(line)):
        if not (line[j].isalnum() or line[j] in ".-"):
            site = line[idx:j].lower()
            break
print(site)"""

#test zip
"""
x = []
for t in zip(range(-10,0,1), range(0,10,2), range(1,10,2)):
    print(t)
    x += t
print(x)
"""

#convert namedtuple into dict
"""import collections

fields=["Id", "ForN", "MidN", "SurN", "Dep"]
User = collections.namedtuple("User", fields)
user_list = User("15", "Mini", "", "Huang", "Admin")
print("{0.Id}".format(user_list))"""

#test range
#ID, FORENAME, MIDNAME, SURNAME, DEPARTMENT = range(5)
#print(MIDNAME)

#test dictionary
#d1 = dict(Forename = "Moore", Surname="Lin", Age=42, Addr="Taipei")
#for item in d1.items():
    #print(type(item))

#test string

#col ="{0:<25} {1:^6} {2:^10}  ".format("Name", "ID", "Username")*2+"\n"
#dash_line = "{0:=<25} {0:=^6} {0:=^10}  ".format("")*2
#title = col + dash_line
#print(title)

#test parameter unpacking
"""def employee_info(**member):
    print(**locals())
    for key in member:
        print("{0} {1}".format(key, member[key]))

new_member1=dict(name="MiMi", age=42, major="CSR"
employee_info(**new_member)"""

#test sorted with lambda
"""import collections
elements=[(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(sorted(elements, key=lambda x: x[1]))
print(sorted(elements, key=lambda x: (x[1],x[2])))
print(sorted(elements, key=lambda x: (x[2],x[1])))

chg_ord = lambda x: (x[1], x[2])
print(sorted(elements, key=chg_ord))

minus_one_dict=collections.defaultdict(lambda: -1)
minus_one_dict.update(name="Moore")
print(minus_one_dict["name"])
print(minus_one_dict["age"])"""

STYLESHEET_TEMPLATE = ('<link rel="stylesheet" type="text/css"'
                       'media="all" href= />\n')
print(STYLESHEET_TEMPLATE)