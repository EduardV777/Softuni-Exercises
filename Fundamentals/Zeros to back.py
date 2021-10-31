str=input()
numbers=[]
k=0
while k<len(str):
    num=""
    if str[k]!="," or str[k]!=" ":
        for j in range(k,len(str)):
            if str[j]!=",":
                k+=1
                num+=str[j]
            else:
                k+=1
                break
        num=int(num)
        numbers.append(num)
    else:
        k+=1
#print(numbers)
k=0; i=0
while k<len(numbers):
    if numbers[k]==0:
        i+=1
        tempVal=numbers[k]
        del numbers[k]
        numbers.append(tempVal)
        if i>len(numbers):
            break
        else:
            continue
    else:
        i=0
        k+=1
print(numbers)
