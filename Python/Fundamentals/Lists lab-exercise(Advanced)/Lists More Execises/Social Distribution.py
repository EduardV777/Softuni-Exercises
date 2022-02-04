population=input(); minWealth=int(input())
population=population.split(", ")
population=[int(e) for e in population]
underMinimumWealth=0; needed=[]; distributionPossible=True
theRich=population.index(max(population))

def genError():
    print("No equal distribution possible")
    return False

for k in range(0,len(population)):
    if population[k]<minWealth:
        underMinimumWealth+=1
        needed.append((minWealth-population[k],k))
for k in range(0,len(needed)):
    #switchy richy
    if population[theRich]<max(population):
        theRich=population.index(max(population))

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
