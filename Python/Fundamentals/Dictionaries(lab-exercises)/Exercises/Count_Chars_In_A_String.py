string=input()
k=0; charsLen={}
while k<len(string):
    if string[k]!=" ":
        charFound=False
        for j in charsLen:
            if j==string[k]:
                charsLen[j]+=1
                charFound=True
        if charFound==False:
            charsLen[string[k]]=1
        k+=1
    else:
        k+=1
output=""
for k in charsLen:
    output+=f"{k} -> {charsLen[k]}\n"
print(output)
