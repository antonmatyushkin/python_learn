import random

article = ['a', 'the', 'an']
noun = ['cat', 'dog', 'man', 'woman']
verb = ['sang', 'run', 'jumped']
adverb = ['loudly', 'quitly', 'well', 'badly']

for i in random.randint(0,1):
    first = str(random.choice(article))
    if i == 0:
        print(first.title()+ " " + str(random.choice(noun)) + " " + str(random.choice(verb)) + ".")
    if i == 1:
        print(first.title() + " " + str(random.choice(noun)) + " " + str(random.choice(verb)) + " " + str(random.choice(adverb)) + "!")