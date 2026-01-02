text=input()
chars={}
for k in range(0,len(text)):
    isCharNew=chars.get(text[k],"not Found")
    if text[k]!=" ":
        if isCharNew=="not Found":
            chars[text[k]]=1
        else:
            chars[text[k]]+=1
for j in chars:
    print(f"{j} -> {chars[j]}")
