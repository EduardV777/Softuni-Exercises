numbers=input()
numbersList=[]; evenNumbersIndices=[]
k=0
while k<len(numbers):
    number=""
    if numbers[k]!=" ":
        for j in range(k,len(numbers)):
            if numbers[j]!=",":
                number+=numbers[j]
                k+=1
            else:
                k+=1
                break
        number=int(number)
        numbersList.append(number)
    else:
        k+=1
#print(numbersList)
for j in range(0,len(numbersList)):
    if numbersList[j]%2==0:
        evenNumbersIndices.append(j)
print(evenNumbersIndices)
