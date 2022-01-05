text=input()
newText=""
for k in range(0,len(text)):
    code=ord(text[k])
    newText+=chr(code+3)
print(newText)
