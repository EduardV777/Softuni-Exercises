data=input()
data=data.split(" "); data=[int(e) for e in data]

while True:
    command=input()
    if command!="end":
        if "exchange" in command:
            command=command.split(" ")
            if int(command[1])<0 or int(command[1])>len(data)-1:
                print("Invalid index")
                continue
            subList1=data[:int(command[1])+1]
            subList2=data[int(command[1])+1:]
            data=list(subList2+subList1)
        elif "max" in command or "min" in command:
            command=command.split(" ")
            lookForMin=False; noMatches=False
            if command[0]=="min":
                lookForMin=True
            if command[1]=="even":
                evenNumbers = [e for e in data if e % 2 == 0]
                if lookForMin==False:
                    if len(evenNumbers)==0:
                        noMatches=True
                    else:
                        maxNum=max(evenNumbers)
                        ind = data.index(maxNum)
                else:
                    if len(evenNumbers)==0:
                        noMatches=True
                    else:
                        minNum=min(evenNumbers)
                        ind = data.index(minNum)
            elif command[1]=="odd":
                oddNumbers = [e for e in data if e % 2 != 0]
                if lookForMin==False:
                    if len(oddNumbers)==0:
                        noMatches=True
                    else:
                        maxNum=max(oddNumbers)
                        ind = data.index(maxNum)
                else:
                    if len(oddNumbers)==0:
                        noMatches=True
                    else:
                        minNum=min(oddNumbers)
                        ind = data.index(minNum)
            if noMatches==True:
                print("No matches")
            else:
                print(ind)
        elif "first" in command or "last" in command:
            command=command.split(" ")
            lookForLast=False; lookForEven=False
            elements=[]; k=0
            if command[0]=="last":
                lookForLast=True
            if command[2]=="even":
                lookForEven=True
            if lookForEven==True:
                if lookForLast==True:
                    if (len(data)-1)-int(command[1])<0:
                        print("Invalid count")
                        continue
                    for j in range(len(data)-1, -1,-1):
                        if k==int(command[1]):
                            break
                        if data[j] % 2 == 0:
                            elements.append(data[j])
                            k+=1
                else:
                    if int(command[1])>len(data)-1:
                        print("Invalid count")
                        continue
                    for j in range(0, len(data)):
                        if k==int(command[1]):
                            break
                        if data[j] % 2 == 0:
                            elements.append(data[j])
                            k+=1
            else:
                if lookForLast==True:
                    if (len(data)-1)-int(command[1])<0:
                        print("Invalid count")
                        continue
                    for j in range(len(data)-1, -1,-1):
                        if k==int(command[1]):
                            break
                        if data[j] % 2 != 0:
                            elements.append(data[j])
                            k+=1
                else:
                    if int(command[1])>len(data)-1:
                        print("Invalid count")
                        continue
                    for j in range(0, len(data)):
                        if k==int(command[1]):
                            break
                        if data[j] % 2 != 0:
                            elements.append(data[j])
                            k+=1
            print(elements)
    else:
        print(data)
        break