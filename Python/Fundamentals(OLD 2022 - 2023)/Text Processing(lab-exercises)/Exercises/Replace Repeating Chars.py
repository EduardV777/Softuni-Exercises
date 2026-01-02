text=input()
editedText=""; previousChar=""
for k in range(0,len(text)):
    if previousChar!=text[k]:
        previousChar=text[k]
        editedText+=text[k]
    else:
        continue
print(editedText)
