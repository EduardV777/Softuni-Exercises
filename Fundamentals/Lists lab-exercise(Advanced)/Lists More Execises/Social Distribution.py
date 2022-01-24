population=input(); minWealth=int(input())
global distributionPossible; distributionPossible=True
population=population.split(", ")
population=[int(e) for e in population]
population.sort()
underMinimumWealth=0; needed=[]
theRich=len(population)-1

def genError():
    print("No equal distribution possible")
    return False

for k in range(0,len(population)):
    if population[k]<minWealth:
        underMinimumWealth+=1
        needed.append((minWealth-population[k],k))
for k in range(0,len(needed)):
    #switchy richy
    if population[theRich]<population[theRich-1]:
        theRich-=1
    elif theRich!=len(population)-1:
        if population[theRich]<population[theRich+1]:
            theRich+=1
    if population[theRich]-needed[k][0]>0:
        population[needed[k][1]]+=needed[k][0]
        population[theRich]-=needed[k][0]
    else:
        distributionPossible=genError()
        break
    if population[theRich]<minWealth:
        distributionPossible=genError()
        break
if distributionPossible==True:
    print(population)
