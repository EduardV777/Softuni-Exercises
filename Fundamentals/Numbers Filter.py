n=int(input())
numbers=[]; filtered=[]
for k in range(1,n+1):
    num=int(input())
    numbers.append(num)
command=input()
if command=="even":
    for k in range(0,len(numbers)):
        if abs(numbers[k])%2==0 or numbers[k]==0:
            filtered.append(numbers[k])
elif command=="odd":
    for k in range(0, len(numbers)):
        if abs(numbers[k])%2!=0:
            filtered.append(numbers[k])
elif command=="negative":
    for k in range(0, len(numbers)):
        if numbers[k]<0:
            filtered.append(numbers[k])
elif command=="positive":
    for k in range(0, len(numbers)):
        if numbers[k]>-1:
            filtered.append(numbers[k])
print(filtered)
