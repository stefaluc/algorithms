# For each letter, which other letter(s) appear in the most words with that letter
# In: List<String> = ['abc', 'bcd', 'cde']
# Out:
#     a: b,c
#     b: c
#     c: b,d
#     d: c
#     e: c,d

# how to use format strings
# "here is some constant text: {} {}".format("1", 2)

# python3 
# print("some text", end='')

def maxLetters(words):
    letters = set()
    for word in words:
        for letter in word:
            if not letter in letters:
                letters.add(letter)
    for letter in letters:
        occurences = {}
        for word in words:
            countedLetters = set()
            if letter in word:
                for l in word:
                    if not l == letter and not l in countedLetters:
                        countedLetters.add(l)
        occurences[l] = occurences.get(l, 0) + 1
        maxLetters = []
        maxOccurences = -1
        for l, number in occurences.items():
            if number > maxOccurences:
                maxOccurences = number
        for l in occurences:
            if occurences[l] == maxOccurences:
                maxLetters.append(l)
        print('{}: '.format(letter), end='')
        for l in maxLetters:
            print('{}, '.format(l), end='')
        print()

words = ['abc', 'bcd', 'cde']
words2 = []
words3 = ['aac', 'cbaa']
maxLetters(words3)
