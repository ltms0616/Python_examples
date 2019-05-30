import random

articles = ["the", "a", "this", "that"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["ate", "drank", "ran", "jumped", "sang"]
adverbs = ["lundly","quietly","well","badly"]

sentense1 = [articles, subjects, verbs, adverbs]
sentense2 = [articles, subjects, verbs]
sentense3 = [verbs, adverbs]
sentense = [sentense1, sentense2, sentense3]


for x in range(5):
    num = random.randint(0,2)
    line = ""
    for y in sentense[num]:
        line += random.choice(y) + " "
    print(line)
