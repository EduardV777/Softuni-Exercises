chars=input()
k=0; char=[]; ascii=[]
while k<len(chars):
    if chars[k]!="," and chars[k]!=" ":
        val=""
        for j in range(k,len(chars)):
            if chars[j]!=",":
                val+=chars[j]
                k+=1
            else:
                break
        char.append(val)
        symbCode=ord(val)
        ascii.append(symbCode)
    else:
        k+=1
charactersDict=dict(zip(char,ascii))
print(charactersDict)
