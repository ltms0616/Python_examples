import string
import sys
import collections

words=collections.defaultdict(int)
strips = string.whitespace + string.punctuation + string.digits + "\"'"

for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strips)
            if len(word)>2:
                words[word] +=1
for word in sorted(words):
    print("'{0}' occurs {1:d} times".format(word, words[word]))