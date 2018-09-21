### remove vowels from input string
text = "abcdefghijklmnopqrstuvwxyz"
letters = set(list(text))
vowels = set(list("aeiou"))
letters.difference_update(vowels)
print(''.join(sorted(letters)))

### answer:
sampleText = "Pyton is a very powerful language"
vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
print(finalSet)
print(sorted(finalSet))