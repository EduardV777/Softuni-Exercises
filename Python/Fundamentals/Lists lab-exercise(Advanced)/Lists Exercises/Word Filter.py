text=input()
words=[]
k=0
while k<len(text):
    word=""
    if text[k]!=" ":
        for j in range(k,len(text)):
            if text[j]!=" ":
                word+=text[j]
                k+=1
            else:
                break
        words.append(word)
    else:
        k+=1
wordsFiltered=list(filter(lambda x: len(x)%2==0,words))
print("\n".join(wordsFiltered))
