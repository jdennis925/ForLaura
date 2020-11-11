from spellchecker import SpellChecker
import itertools

spell = SpellChecker()

letters = input("Input today's letters:\n")
mustContainLetter = input("Must contain letter:\n")

wordTries = list()

for index in range(5, 10):
    permSets = list(itertools.product(letters, repeat=index))

    for col in permSets:
        s = ""
        s = s.join(col)
        if(mustContainLetter in s):
            wordTries.append(s)

words = spell.known(wordTries)

print("Word Count: " + str(len(words)))
for word in sorted(words, key=len):
        print(word)