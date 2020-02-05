import random
article = ["the", "a", "an"]
subject = ["cat", "dog", "man", "woman"]
verb = ["ate", "ran", "laughed", "jumped"]
adverb = ["loudly", "quietly", "well", "badly"]
sentences = [[article, subject, verb, adverb], [article, subject, verb]]

def get_poem_rows(msg, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            else:
                num = int(line)
                return num
        except ValueError as err:
            print(err)

rows = get_poem_rows("Enter the no. of rows of poem or Enter for 5:", 5)
for i in range(rows):
    type = random.randint(0, 1)
    sentence = sentences[type]
    line = ""
    for j in range(len(sentence)):
        line += random.choice(sentence[j]) + " "
    print(line)

