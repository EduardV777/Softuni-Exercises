giftsToBuy=input()
giftsList=[]
k=0
while k<len(giftsToBuy):
    giftName=""
    if giftsToBuy[k]!=" ":
        for j in range(k,len(giftsToBuy)):
            if giftsToBuy[j]!=" ":
                giftName+=giftsToBuy[j]
                k+=1
            else:
                k+=1
                break
        giftsList.append(giftName)
    else:
        k+=1
#print(giftsList)
command=""
while command!="No Money":
    command=input()
    if command!="No Money":
        if command.find("OutOfStock")!=-1:
            giftName=""
            for j in range(10,len(command)):
                if command[j]!=" ":
                    giftName+=command[j]
            for j in range(0,len(giftsList)):
                if giftsList[j]==giftName:
                    giftsList[j]="None"
        elif command.find("Required")!=-1:
            giftName=""; index=""; stoppedAt=0
            for j in range(9,len(command)):
                if command[j]!=" ":
                    giftName+=command[j]
                else:
                    stoppedAt=j
                    break
            for j in range(stoppedAt+1,len(command)):
                if command[j]!=" ":
                    index+=command[j]
            index=int(index)
            if not index>len(giftsList)-1 or index<0:
                giftsList[index]=giftName
        elif command.find("JustInCase")!=-1:
            giftName=""
            for j in range(11,len(command)):
                if command[j]!=" ":
                    giftName+=command[j]
            giftsList[len(giftsList)-1]=giftName
j=0
while j<len(giftsList):
    if giftsList[j]=="None":
        del giftsList[j]
        continue
    j+=1
print(" ".join(giftsList))
