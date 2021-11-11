str1=input(); str2=input()
seq1=[]
k=0
while k<len(str1):
    str=""
    if str1[k]!=" ":
        for j in range(k,len(str1)):
            if str1[j]!=",":
                str+=str1[j]
                k+=1
            else:
                k+=1
                break
        seq1.append(str)
    else:
        k+=1
filtered=list(filter(lambda x: x in str2,seq1))
print(filtered)
