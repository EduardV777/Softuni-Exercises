numbers=input()
numbersList=[]; largestNumber=0
k=0
while k<len(numbers):
    num=""
    if numbers[k]!=" ":
        for j in range(k,len(numbers)):
            if numbers[j]!=" ":
                num+=numbers[j]
                k+=1
            else:
                k+=1
                break
        numbersList.append(num)
    else:
        k+=1
        break
numbersList.sort()
numbersList.reverse()
largestNumber="".join(numbersList)
print(largestNumber)
