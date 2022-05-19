from collections import deque

circleRoute=deque([])
n=int(input()); k=0
startingPoint=0; startPointFound=False

while k<n:
    #amountOfPetrol distancetoNextPump
    data=input(); data=data.split(" ")
    amountOfPetrol=int(data[0]); distanceToNext=int(data[1])
    circleRoute.append([amountOfPetrol, distanceToNext, k])
    k+=1

#print(circleRoute)

while startPointFound==False:
    start=circleRoute.popleft()
    circleRoute.append(start)
    tankInsufficient=False
    tank=start[0]
    routePoint=-1
    if tank>=start[1]:
        tank-=start[1]
        while True:
            routePoint=circleRoute.popleft()
            circleRoute.append(routePoint)
            if routePoint[2]!=start[2]:
                tank+=routePoint[0]
                if tank>=routePoint[1]:
                    tank-=routePoint[1]
                else:
                    tankInsufficient=True
                    break
            else:
                break
    else:
        tankInsufficient=True
    if tankInsufficient==False:
        startingPoint=start[2]
        break

print(startingPoint)