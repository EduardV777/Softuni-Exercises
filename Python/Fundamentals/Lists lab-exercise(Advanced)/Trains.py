nWagons=int(input())
train=[]
for j in range(0,nWagons):
    train.append(0)
#print(train)
command=""
while command!="End":
    command=input()
    if command!="End":
        if command.find("add")!=-1:
            nPeople=""
            for j in range(4,len(command)):
                nPeople+=command[j]
            nPeople=int(nPeople)
            train[len(train)-1]+=nPeople
        elif command.find("insert")!=-1:
            index=""; nPeople=""; stoppedAt=0
            for j in range(7,len(command)):
                if command[j]!=" ":
                    index+=command[j]
                else:
                    stoppedAt=j
                    break
            for j in range(stoppedAt+1,len(command)):
                nPeople+=command[j]
            index=int(index); nPeople=int(nPeople)
            train[index]+=nPeople
        elif command.find("leave")!=-1:
            index=""; nPeople=""; stoppedAt=0
            for j in range(6,len(command)):
                if command[j]!=" ":
                    index+=command[j]
                else:
                    stoppedAt=j
                    break
            for j in range(stoppedAt+1,len(command)):
                nPeople+=command[j]
            index=int(index); nPeople=int(nPeople)
            train[index]-=nPeople
print(train)
