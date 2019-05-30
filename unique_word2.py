import sys
import string
import collections

words= collections.defaultdict(int)

strips = string.digits+string.whitespace+string.punctuation+'\n'

for line in open("word_counts.txt", encoding="utf8"):
    for word in line.lower().split():
        word = word.strip(strips)
        if len(word) > 2:
            #words[word] = words.get(word,0)+1
            words[word] += 1

def chg_ord(x):
    return x[1]

for word, count in sorted(words.items(), key=chg_ord):
    print("'{}' occurs {} times".format(word, count))

#for word, count in sorted(words.items(), key=lambda x:x[1], reverse=True):
    #print("'{}' occurs {} times".format(word, count))
