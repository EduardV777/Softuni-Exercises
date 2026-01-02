str=input()
invertedVal=[]
k=0
while k<len(str):
    invertNum=""
    if str[k]==" ":
        k += 1
        continue
    elif str[k]=="-":
        k+=1
        for j in range(k,len(str)):
            if str[j]==" ":
                k += 1
                break
            else:
                k += 1
                invertNum+=str[j]
        invertNum=int(invertNum)
        invertedVal.append(invertNum)
    elif str[k].isdigit():
        for j in range(k,len(str)):
            if str[j]==" ":
                k += 1
                break
            else:
                k += 1
                invertNum+=str[j]
        invertNum = int(invertNum)
        invertNum *= -1
        invertedVal.append(invertNum)
print(invertedVal)
