secretMsg=input()
msgPieces=[]
k=0
while k<len(secretMsg):
    word=""
    if secretMsg[k]!=" ":
        for j in range(k,len(secretMsg)):
            if secretMsg[j]!=" ":
                word+=secretMsg[j]
                k+=1
            else:
                break
        msgPieces.append(word)
    else:
        k+=1

for k in range(0,len(msgPieces)):
    code=""; characters=""
    for j in range(0,len(msgPieces[k])):
        if msgPieces[k][j].isdigit()==True:
            code+=msgPieces[k][j]
        elif msgPieces[k][j].isalpha()==True:
            characters+=msgPieces[k][j]
    code=int(code)
    code=chr(code)
    decryptedWord=code+characters
    msgPieces[k]=decryptedWord
for k in range(0,len(msgPieces)):
    word=[]
    for j in range(0,len(msgPieces[k])):
        word.append(msgPieces[k][j])
    temp=word[1]; word[1]=word[len(word)-1]; word[len(word)-1]=temp
    msgPieces[k]="".join(word)
print(" ".join(msgPieces))
