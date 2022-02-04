factor=int(input()); count=int(input())
numbers=[]
j=1
for k in range(1,count+1):
    while True:
        if j%factor==0:
            numbers.append(j)
            j+=1
            break
        else:
            j+=1
            continue
print(numbers)
