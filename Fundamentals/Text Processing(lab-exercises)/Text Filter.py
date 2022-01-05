banWords=input(); text=input()
banWordsList=banWords.split(", ")
for k in range(0,len(banWordsList)):
    while True:
        if banWordsList[k] in text:
            wordLen=len(banWordsList[k])
            replaceWith="*"*wordLen
            text=text.replace(banWordsList[k],replaceWith)
        else:
            break
print(text)
