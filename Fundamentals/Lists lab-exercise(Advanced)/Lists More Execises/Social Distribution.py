population=input(); minWealth=int(input())
popWealth=[]
k=0; equalDistribution=True
while k<len(population):
    val=""
    if population[k]!=" ":
        for j in range(k,len(population)):
            if population[j]!=",":
                val+=population[j]
                k+=1
            else:
                k+=1
                break
        val=int(val)
        popWealth.append(val)
    else:
        k+=1

maxWealth=0
for j in range(0,len(popWealth)):
    if popWealth[maxWealth]<popWealth[j]:
        maxWealth=j
for k in range(0,len(popWealth)):
    if popWealth[k]<minWealth:
        diff=minWealth-popWealth[k]
        popWealth[k]=minWealth
        if popWealth[maxWealth]-diff>=minWealth:
            popWealth[maxWealth]-=diff
        else:
            maxWealth=0
            for j in range(0,len(popWealth)):
                if popWealth[maxWealth]<popWealth[j]:
                    maxWealth=j
            popWealth[maxWealth]-=diff
for i in range(0,len(popWealth)):
    if popWealth[i]<minWealth:
        print("No equal distribution possible")
        equalDistribution=False
        break
if equalDistribution==True:
    print(popWealth)
