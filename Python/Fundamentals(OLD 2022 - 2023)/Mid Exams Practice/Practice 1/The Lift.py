people=int(input()); liftState=input()
liftState=liftState.split(" ")
liftState=[int(e) for e in liftState]

k=0
while k<len(liftState):
    if people==0:
        break
    if liftState[k]!=4:
        people-=1; liftState[k]+=1
        continue
    else:
        k+=1
noEmptySpots=True
for k in range(0,len(liftState)):
    if liftState[k]!=4:
        noEmptySpots=False

if people==0 and noEmptySpots==False:
    liftState = [str(e) for e in liftState]
    print(f"The lift has empty spots!\n{' '.join(liftState)}")
elif people!=0 and noEmptySpots==True:
    liftState = [str(e) for e in liftState]
    print(f"There isn't enough space! {people} people in a queue!\n{' '.join(liftState)}")
elif people==0 and noEmptySpots==True:
    liftState = [str(e) for e in liftState]
    print(f"{' '.join(liftState)}")
