import sys
import unicodedata

def print_unicode_table(word):
    print("{:^7}  {:^5}  {:^3}  {:^40}".format("decimal","hex","chr","name"))
    print("{0:^.7}  {0:^.5}  {0:^.3}  {0:^.40}".format("="*40))

    code = 0
    max_code = min(0xd800, sys.maxunicode)

    if word in ("-a", "--all"):
        while code < max_code:
            c=chr(code)
            name=unicodedata.name(c, "*****unknown*****")
            print("{0:>7}  {0:>5X}  {0:>3c}  {1:<40}".format(code, name.title()))
            code+=1
    else:
        code = ord(word)
        name = unicodedata.name(word, "*****unknown*****")
        print("{0:>7}  {0:>5X}  {0:^3c}  {1:<40}".format(code, name.title()))

word=""
if len(sys.argv) > 1:
    if sys.argv[1] in ("h","--help"):
        print("usage: print_unicode_table [word]")
    else:
        word = sys.argv[1].lower()
        print(word)
if word != 0:
    print_unicode_table(word)