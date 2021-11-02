seq=input()
integersList=[]; command=""
k=0
while k<len(seq):
    num=""
    if seq[k]!=" ":
        for j in range(k,len(seq)):
            if seq[j]!=" ":
                num+=seq[j]
                k+=1
            else:
                k+=1
                break
        num=int(num)
        integersList.append(num)
    else:
        k+=1
#print(integersList)
while command!="end":
    command=input()
    if command!="end":
        if command.find("exchange")!=-1:
            start=command.find("exchange"); start+=8
            ind=""
            for j in range(start,len(command)):
                ind+=command[j]
            ind=int(ind)
            if ind<0 or ind>len(integersList):
                print("Invalid index")
            else:
                if len(integersList)>1:
                    list1=[];list2=[]
                    #splitting list in two at the index that was given
                    for j in range(0,ind+1):
                        list1.append(integersList[j])
                    for j in range(ind+1,len(integersList)):
                        list2.append(integersList[j])
                    #exchanging values from both separate lists
                    for j in range(0,len(list2)):
                        integersList[j]=list2[j]
                    i=0
                    for j in range(len(list2),len(integersList)):
                        integersList[j]=list1[i]
                        i+=1
                else:
                    continue
                #print(integersList)
        elif command.find("max")!=-1 or command.find("min")!=-1:
            if command.find("max")!=-1:
                searchingMax=True
            else:
                searchingMax=False
            list1=[]; notFound=False
            if command.find("even")!=-1:
                for j in range(0,len(integersList)):
                    if integersList[j]%2==0:
                        list1.append(integersList[j])
                    else:
                        continue
                if len(list1)>0:
                    maxNum=max(list1)
                    minNum=min(list1)
                    maxNumIndex = integersList.index(maxNum); minNumIndex = integersList.index(minNum)
                else:
                    print("No matches")
                    notFound=True
            elif command.find("odd")!=-1:
                for j in range(0,len(integersList)):
                    if integersList[j]%2!=0:
                        list1.append(integersList[j])
                    else:
                        continue
                if len(list1)>0:
                    maxNum=max(list1)
                    minNum=min(list1)
                    maxNumIndex=integersList.index(maxNum); minNumIndex=integersList.index(minNum)
                else:
                    print("No matches")
                    notFound=True
            if notFound==False:
                if searchingMax==True:
                    print(maxNumIndex)
                else:
                    print(minNumIndex)
        elif command.find("first")!=-1 or command.find("last")!=-1:
            if command.find("first")!=1:
                requestingFirst=True
            else:
                requestingFirst=False
            if requestingFirst==True:
                start=command.find("first"); start+=6
                count=""
                for j in range(start,len(command)):
                    if command[j]!=" ":
                        count+=command[j]
                    else:
                        break
                count=int(count); list1=[]; j=0; i=0
                if count>len(integersList):
                    print("Invalid count")
                    continue
                if command.find("even")!=-1:
                    while i<count:
                        if j>len(integersList)-1:
                            break
                        if integersList[j]%2==0:
                            list1.append(integersList[j])
                            i+=1; j+=1
                        else:
                            j+=1
                            continue
                elif command.find("odd")!=-1:
                    while i<count:
                        if j>len(integersList)-1:
                            break
                        if integersList[j]%2!=0:
                            list1.append(integersList[j])
                            i+=1; j+=1
                        else:
                            j+=1
                            continue
                print(list1)
            else:
                start = command.find("last"); start += 5
                count = ""
                for j in range(start, len(command)):
                    if command[j] != " ":
                        count += command[j]
                    else:
                        break
                count = int(count); list1 = []; j = 0; i=0
                if command.find("even") != -1:
                    while i<count:
                        if j>len(integersList)-1:
                            break
                        if integersList[j] % 2 == 0:
                            list1.append(integersList[j])
                            i+=1; j += 1
                        else:
                            j+=1
                            continue
                elif command.find("odd") != -1:
                    while i<count:
                        if j>len(integersList)-1:
                            break
                        if integersList[j] % 2 != 0:
                            list1.append(integersList[j])
                            i+=1; j += 1
                        else:
                            j+=1
                            continue
                print(list1)
    else:
        break
print(integersList)
