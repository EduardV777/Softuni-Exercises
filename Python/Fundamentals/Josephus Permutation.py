lineOfPeople=input(); skip=int(input())
orderPeople=[]; orderExecutions=[]
k=0
while k<len(lineOfPeople):
    num=""
    if lineOfPeople[k]!=" ":
        for j in range(k,len(lineOfPeople)):
            if lineOfPeople[j]!=" ":
                num+=lineOfPeople[j]
                k+=1
            else:
                k+=1
                break
        num=int(num)
        orderPeople.append(num)
    else:
        k+=1
#print(orderPeople)
nextExecution=skip-1
k=0
while k<len(orderPeople):
    i=0
    if nextExecution+1>len(orderPeople) and k==0:
        nextExecution-=len(orderPeople)
    if k==nextExecution:
        orderExecutions.append(orderPeople[k])
        del orderPeople[k]
        while i<skip-1:
            if nextExecution==len(orderPeople) and len(orderPeople)!=0:
                nextExecution=0
                continue
            if nextExecution==len(orderPeople)-1:
                nextExecution=-1
            nextExecution+=1
            i+=1
        if not k<len(orderPeople):
            k=0
    else:
        k+=1
        if k>len(orderPeople)-1:
            k=0
for j in range(0,len(orderExecutions)):
    orderExecutions[j]=str(orderExecutions[j])
orderOutput="["; orderOutput+=",".join(orderExecutions); orderOutput+="]"
print(orderOutput)
