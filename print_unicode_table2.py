import sys
import unicodedata

def print_unicode_table(words):
    print("{:^7}  {:^5}  {:^3}  {:^40}".format("decimal","hex","chr","name"))
    print("{0:^.7}  {0:^.5}  {0:^.3}  {0:^.40}".format("="*40))

    code = 0
    max_code = min(0xd800, sys.maxunicode)

    while code < max_code:
        c = chr(code)
        flag = True
        name = unicodedata.name(c, "*****unknown*****")
        if not words or words[0] in ("-a", "--all"):
            print("{0:>7}  {0:>5X}  {0:>3c}  {1:<40}".format(code, name.title()))
        else:
            for word in words:
                if word not in name.title():
                    flag = False
            if flag:
                print("{0:>7}  {0:>5X}  {0:>3c}  {1:<40}".format(code, name.title()))
        code += 1

    """if not words or words[1] in ("-a", "--all"):
        while code < max_code:
            c = chr(code)
            name = unicodedata.name(c, "*****unknown*****")
            print("{0:>7}  {0:>5X}  {0:>3c}  {1:<40}".format(code, name.title()))
            code += 1
    else:
        while code < max_code:
        code = ord(word)
        name = unicodedata.name(word, "*****unknown*****")
        print("{0:>7}  {0:>5X}  {0:^3c}  {1:<40}".format(code, name.title())"""

words=[]
word=""
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h","--help"):
        print("usage: print_unicode_table [word]")
    else:
        for x in range(1,len(sys.argv)):
            word = sys.argv[x]
            words.append(word)
        print(words)
        print_unicode_table(words)