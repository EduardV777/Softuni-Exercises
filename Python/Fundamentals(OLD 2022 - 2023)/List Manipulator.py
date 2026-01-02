initList=input()
initList=initList.split(" "); initList=[int(e) for e in initList]
while True:
    command=input()
    if command!="end":

        if "exchange" in command:
            command=command.split(" ")
            index=int(command[1])
            if index<0 or index>len(initList):
                print("Invalid index")
                continue
            subList1=initList[index+1:]; subList2=initList[0:index+1]
            initList=subList1+subList2

        elif "max" in command:
            if "even" in command:
                maxEven=[e for e in initList if e%2==0]
                if len(maxEven)==0:
                    print("No matches")
                    continue
                maxEven=max(maxEven)
                indexOfNum=initList.index(maxEven)
                print(indexOfNum)
            elif "odd" in command:
                maxOdd=[e for e in initList if e%2!=0]
                if len(maxOdd)==0:
                    print("No matches")
                    continue
                maxOdd=max(maxOdd)
                indexOfNum=initList.index(maxOdd)
                print(indexOfNum)

        elif "min" in command:
            if "even" in command:
                minEven=[e for e in initList if e%2==0]
                if len(minEven)==0:
                    print("No matches")
                    continue
                minEven=min(minEven)
                indexOfNum=initList.index(minEven)
                print(indexOfNum)
            elif "odd" in command:
                minOdd=[e for e in initList if e%2!=0]
                if len(minOdd)==0:
                    print("No matches")
                    continue
                minOdd=min(minOdd)
                indexOfNum=initList.index(minOdd)
                print(indexOfNum)

        elif "first" in command:
            if "even" in command:
                command=command.split(" "); command[1]=int(command[1])
                if command[1]>len(initList):
                    print("Invalid count")
                    continue
                evenNumbers=[e for e in initList if e%2==0]
                pickedNumbers=[]
                k=0
                while k<len(evenNumbers):
                    if command[1]==0:
                        break
                    pickedNumbers.append(evenNumbers[k])
                    k+=1; command[1]-=1
                print(pickedNumbers)

            elif "odd" in command:
                command=command.split(" "); command[1]=int(command[1])
                if command[1]>len(initList):
                    print("Invalid count")
                    continue
                oddNumbers=[e for e in initList if e%2!=0]
                pickedNumbers=[]
                k=0
                while k<len(oddNumbers):
                    if command[1]==0:
                        break
                    pickedNumbers.append(oddNumbers[k])
                    k+=1; command[1]-=1
                print(pickedNumbers)

        elif "last" in command:
            if "even" in command:
                command=command.split(" "); command[1]=int(command[1])
                if command[1]>len(initList):
                    print("Invalid count")
                    continue
                evenNumbers=[e for e in initList if e%2==0]
                pickedNumbers=[]
                k=len(evenNumbers)-1
                while k>-1:
                    if command[1]==0:
                        break
                    pickedNumbers.append(evenNumbers[k])
                    k-=1; command[1]-=1
                print(pickedNumbers)

            elif "odd" in command:
                command = command.split(" "); command[1] = int(command[1])
                if command[1] > len(initList):
                    print("Invalid count")
                    continue
                oddNumbers = [e for e in initList if e % 2 != 0]
                pickedNumbers = []
                k = len(oddNumbers) - 1
                while k > -1:
                    if command[1] == 0:
                        break
                    pickedNumbers.append(oddNumbers[k])
                    k -= 1; command[1] -= 1
                print(pickedNumbers)
    else:
        print(initList)
        break
