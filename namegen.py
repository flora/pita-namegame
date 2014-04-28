#!/usr/bin/python
import sys, json, random

words = json.load(sys.stdin)

nouns = []
adjectives = []

for w, pos in words.iteritems():
    if pos == 'noun':
        nouns.append(w)
    else:
        adjectives.append(w)

for x in range(100):
    first_word = random.choice(nouns) if bool(random.getrandbits(1)) else random.choice(adjectives)
    second_word = random.choice(nouns)
    name = first_word + ' ' + second_word
    name = name.title()
    print name
