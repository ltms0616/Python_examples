import sys
import string

words={}

strips = string.digits+string.whitespace+string.punctuation+'\n'

for line in open("word_counts.txt", encoding="utf8"):
    for word in line.lower().split():
        word = word.strip(strips)
        if len(word) > 2:
            words[word] = words.get(word,0)+1

for word, count in sorted(words.items()):
    print("'{}' occurs {} times".format(word, count))
