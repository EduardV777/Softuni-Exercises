data=input()
data=data.split(" "); data=[int(e) for e in data]

while True:
    command=input()
    if command!="end":
        if "exchange" in command:
            command=command.split(" ")
            if int(command[1])<0 or int(command[1])>len(data):
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
                        ind = data.index(max(evenNumbers))
                else:
                    if len(evenNumbers)==0:
                        noMatches=True
                    else:
                        ind = data.index(min(evenNumbers))
            elif command[1]=="odd":
                oddNumbers = [e for e in data if e % 2 != 0]
                if lookForMin==False:
                    if len(oddNumbers)==0:
                        noMatches=True
                    else:
                        ind = data.index(max(oddNumbers))
                else:
                    if len(oddNumbers)==0:
                        noMatches=True
                    else:
                        ind = data.index(min(oddNumbers))
            if noMatches==True:
                print("No matches")
            else:
                print(ind)
        elif "first" in command or "last" in command:
            command=command.split(" ")
            lookForLast=False; lookForEven=False
            elements=[]
            if command[0]=="last":
                lookForLast=True
            if command[0]=="first" or command[0]=="last":
                if int(command[1])>len(data) or int(command[1])<0:
                    print("Invalid count")
                    continue
                else:
                    if command[2]=="even":
                        lookForEven=True
                    if lookForEven==True:
                        if lookForLast==True:
                            for k in range(len(data)-1, len(data)-int(command[1])-2,-1):
                                if data[k] % 2 == 0:
                                    elements.append(data[k])
                        else:
                            for k in range(0, 0+int(command[1])):
                                if data[k] % 2 == 0:
                                    elements.append(data[k])
                    else:
                        if lookForLast==True:
                            for k in range(len(data)-1, len(data)-int(command[1])-2,-1):
                                if data[k] % 2 != 0:
                                    elements.append(data[k])
                        else:
                            for k in range(0, 0+int(command[1])):
                                if data[k] % 2 != 0:
                                    elements.append(data[k])
                print(elements)
    else:
        print(data)
        break
