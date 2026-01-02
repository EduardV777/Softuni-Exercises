numbers=input()
numbersList=[]
k=0
while k<len(numbers):
    num=""
    if numbers[k]!=" ":
        for j in range(k,len(numbers)):
            if numbers[j]!=",":
                num+=numbers[j]
                k+=1
            else:
                k+=1
                break
        num=int(num)
        numbersList.append(num)
    else:
        k+=1
positiveNumbers=list(filter(lambda x: x>-1,numbersList))
negativeNumbers=list(filter(lambda x: x<0,numbersList))
evenNumbers=list(filter(lambda x: x%2==0,numbersList))
oddNumbers=list(filter(lambda x: x%2!=0,numbersList))
for k in range(0,len(positiveNumbers)):
    positiveNumbers[k]=str(positiveNumbers[k])
for k in range(0,len(negativeNumbers)):
    negativeNumbers[k]=str(negativeNumbers[k])
for k in range(0,len(evenNumbers)):
    evenNumbers[k]=str(evenNumbers[k])
for k in range(0,len(oddNumbers)):
    oddNumbers[k]=str(oddNumbers[k])
print(f"Positive: {', '.join(positiveNumbers)}\nNegative: {', '.join(negativeNumbers)}\nEven: {', '.join(evenNumbers)}\nOdd: {', '.join(oddNumbers)}")
