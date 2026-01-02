word = input()
wordRev = ""

for k in range(len(word) - 1, -1, -1):
    wordRev += word[k]

print(wordRev)