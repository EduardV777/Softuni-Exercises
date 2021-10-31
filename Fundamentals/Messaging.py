numbers=input(); str=input()
msg=""; indexesList=[]; str1=[]
for k in range(0,len(str)):
    str1.append(str[k])
k=0
while k<len(numbers):
    num=""; index=0
    if numbers[k]!=" ":
        for j in range(k,len(numbers)):
            if numbers[j]!=" ":
                num+=numbers[j]
                k+=1
            else:
                k+=1
                break
        for j in range(0,len(num)):
            index+=int(num[j])
        indexesList.append(index)
    else:
        k+=1
        break
k=0
while k<len(indexesList):
    j=0
    while j<indexesList[k]:
        if j < len(str1):
            j+=1
            if j == indexesList[k]:
                ind = j
                break
        else:
            indexesList[k]-=j
            j=0
    msg+=str1[ind]
    del str1[j]
    k+=1
print(msg)
