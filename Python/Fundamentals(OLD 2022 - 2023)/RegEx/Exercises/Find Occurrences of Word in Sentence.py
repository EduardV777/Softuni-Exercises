import re
sentence=input()
wordToSearch=input()
counter=re.compile(fr"\b{wordToSearch}+\b", re.I)
occurrences=counter.findall(sentence)
print(len(occurrences))
