list1=input()
list1=list1.split(" ")
for k in range(0,len(list1)):
    list1[k]=int(list1[k])
while True:
    command=input()
    if command!="end":
        if "exchange" in command:
            command=command.split(" ")
            if -1<int(command[1])<len(list1):
                subList=[]; k=int(command[1])+1
                while k<len(list1):
                    subList.append(list1[k])
                    del list1[k]
                subList.reverse()
                for k in range(0,len(subList)):
                    list1.insert(0,subList[k])
            else:
                print("Invalid index")
        elif "max" in command:
            if "odd" in command:
                oddElements=[]
                for k in range(0,len(list1)):
                    if list1[k]%2!=0:
                        oddElements.append(list1[k])
                if len(oddElements)>0:
                    maxNum=max(oddElements)
                    ind=list1.index(maxNum)
                    print(ind)
                else:
                    print("No matches")
            elif "even" in command:
                evenElements=[]
                for k in range(0,len(list1)):
                    if list1[k]%2==0:
                        evenElements.append(list1[k])
                if len(evenElements)>0:
                    maxNum=max(evenElements)
                    ind=list1.index(maxNum)
                    print(ind)
                else:
                    print("No matches")
        elif "min" in command:
            if "odd" in command:
                oddElements = []
                for k in range(0, len(list1)):
                    if list1[k]%2!=0:
                        oddElements.append(list1[k])
                if len(oddElements)>0:
                    minNum = min(oddElements)
                    ind = list1.index(minNum)
                    print(ind)
                else:
                    print("No matches")
            elif "even" in command:
                evenElements = []
                for k in range(0, len(list1)):
                    if list1[k]%2==0:
                        evenElements.append(list1[k])
                if len(evenElements)>0:
                    minNum = min(evenElements)
                    ind = list1.index(minNum)
                    print(ind)
                else:
                    print("No matches")
        elif "first" in command:
            if "odd" in command:
                command=command.split(" "); oddElements=[]
                count=int(command[1])
                if count>=len(list1):
                    print("Invalid count")
                else:
                    k=0
                    while k<len(list1):
                        if count==0:
                            break
                        if list1[k]%2!=0:
                            oddElements.append(list1[k])
                            count-=1
                        k+=1
                    print(oddElements)
            elif "even" in command:
                command = command.split(" "); evenElements = []
                count = int(command[1])
                if count>=len(list1):
                    print("Invalid count")
                else:
                    k = 0
                    while k < len(list1):
                        if count==0:
                            break
                        if list1[k] % 2 == 0:
                            evenElements.append(list1[k])
                            count -= 1
                        k+=1
                    print(evenElements)

        elif "last" in command:
            if "odd" in command:
                command=command.split(" "); oddElements=[]
                count=int(command[1])
                if len(list1)-count<0:
                    print("Invalid count")
                else:
                    k=len(list1)-1
                    while k>=0:
                        if count==0:
                            break
                        if list1[k]%2!=0:
                            oddElements.append(list1[k])
                            count-=1
                        k-=1
                    print(oddElements)
            elif "even" in command:
                command = command.split(" "); evenElements = []
                count = int(command[1])
                if len(list1)-count<0:
                    print("Invalid count")
                else:
                    k = len(list1)-1
                    while k >= 0:
                        if count==0:
                            break
                        if list1[k] % 2 == 0:
                            evenElements.append(list1[k])
                            count -= 1
                        k-=1
                    print(evenElements)
    else:
        print(list1)
        break
