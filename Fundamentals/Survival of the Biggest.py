numbers=input(); n=int(input())
numbersList=[]
k=0; output=""
while k<len(numbers):
    num=""
    if numbers[k]!=" ":
        for j in range(k,len(numbers)):
            if numbers[j]==" ":
                k+=1
                break
            else:
                k+=1
                num+=numbers[j]
        numbersList.append(int(num))
    else:
        k+=1
        break
for k in range(0,n):
    for j in range(0,len(numbersList)):
        num=min(numbersList)
        if numbersList[j]==num:
            del numbersList[j]
            break
for k in range(0,len(numbersList)):
    if k==len(numbersList)-1:
        output += str(numbersList[k])
    else:
        output+=str(numbersList[k])+", "
print(output)
