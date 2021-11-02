seq=input()
absList=[]
k=0
while k<len(seq):
    num=""
    if seq[k]!=" ":
        for j in range(k,len(seq)):
            if seq[j]!=" ":
                num+=seq[j]
                k+=1
            else:
                k+=1
                break
        num=abs(float(num))
        absList.append(num)
    else:
        k+=1
        break
print(absList)
