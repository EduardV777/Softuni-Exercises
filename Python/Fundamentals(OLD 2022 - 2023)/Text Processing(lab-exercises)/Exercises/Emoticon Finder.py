text=input()
emoticons=[]
ind=0
while True:
    ind=text.find(":",ind)
    if ind==-1:
        break
    else:
        emoticons.append(text[ind]+text[ind+1])
        ind+=1
print("\n".join(emoticons))
