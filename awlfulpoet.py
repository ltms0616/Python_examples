import random

article = ["the", "a", "an"]
subject = ["cat", "dog", "man", "woman"]
verb = ["ate", "ran", "laughed", "jumped"]
adverb = ["loudly", "quietly", "well", "badly"]
sentences = [[article, subject, verb, adverb], [article, subject, verb]]

for i in range(5):
    type = random.randint(0, 1)
    sentence = sentences[type]
    line = ""
    for j in range(len(sentence)):
        line += random.choice(sentence[j]) + " "
    print(line)

