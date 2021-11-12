targets=input()
targetList=[]
k=0
while k<len(targets):
    val=""
    if targets[k]!=" ":
        for j in range(k,len(targets)):
            if targets[j]!=" ":
                val+=targets[j]
                k+=1
            else:
                break
        val=int(val)
        targetList.append(val)
    else:
        k+=1

command=""
while command!="End":
    command=input()
    if command!="End":

        if "Shoot" in command:
            index=""; power=""
            k=6; stoppedAt=0
            while k<len(command):
                if command[k]!=" ":
                    for j in range(k,len(command)):
                        if command[j]!=" ":
                            if stoppedAt==0:
                                index+=command[j]
                                k+=1
                            else:
                                power+=command[j]
                                k+=1
                        else:
                            break
                else:
                    k+=1
                    stoppedAt=k
            index=int(index); power=int(power)
            if -1<index<len(targetList):
                targetList[index]-=power
                if targetList[index]<=0:
                    del targetList[index]

        elif "Add" in command:
            index=""; val=""
            k=4; stoppedAt=0
            while k<len(command):
                if command[k]!=" ":
                    for j in range(k,len(command)):
                        if command[j]!=" ":
                            if stoppedAt==0:
                                index+=command[j]
                                k+=1
                            else:
                                val+=command[j]
                                k+=1
                        else:
                            break
                else:
                    k+=1
                    stoppedAt=k
            index=int(index); val=int(val)
            if -1<index<len(targetList):
                targetList.insert(index,val)
            else:
                print("Invalid placement!")

        elif "Strike" in command:
            index=""; radius=""
            k=7; stoppedAt=0
            while k<len(command):
                if command[k]!=" ":
                    for j in range(k,len(command)):
                        if command[j]!=" ":
                            if stoppedAt==0:
                                index+=command[j]
                                k+=1
                            else:
                                radius+=command[j]
                                k+=1
                        else:
                            break
                else:
                    k+=1
                    stoppedAt=k
            index=int(index); radius=int(radius)
            if -1<index<len(targetList):
                if radius>0:
                    if (index-1)-radius>-2 and (index+1)+radius<len(targetList):
                        for j in range(index-1,(index-1)-radius,-1):
                            targetList[j]="Striked"
                        for j in range(index+1,(index+1)+radius,+1):
                            targetList[j]="Striked"
                    else:
                        print("Strike missed!")
                        continue
                del targetList[index]
                j=0
                while j<len(targetList):
                    if targetList[j]=="Striked":
                        del targetList[j]
                        continue
                    j+=1
            else:
                print("Strike missed!")
for k in range(0,len(targetList)):
    targetList[k]=str(targetList[k])
print("|".join(targetList))
