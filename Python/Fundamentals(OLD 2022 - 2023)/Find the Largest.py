num=input()
number=[]; maxNum=0
for k in range(0,len(num)):
    number.append(num[k])
k=len(number)
#sorting here
for k in range(1,k):
    for j in range(0,len(number)-k):
        if number[j]<number[j+1]:
            temp=number[j]
            number[j]=number[j+1]
            number[j+1]=temp
print("".join(number))
