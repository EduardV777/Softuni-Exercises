words=[]
while True:
    word=input()
    if word!="end":
        words.append(word)
    else:
        break
for k in range(0,len(words)):
    reversedWord=""
    for ch in reversed(words[k]):
        reversedWord+=ch
    print(f"{words[k]} = {reversedWord}")
