contestsData={}; individualData={}
while True:
    data=input()
    if data!="no more time":
        dataList=data.split(" -> ")
        username=dataList[0]; contest=dataList[1]; pts=dataList[2]
        contestFound=False; userFound=False
        for j in contestsData:
            if j==contest:
                contestFound=True
                for k in range(0,len(contestsData[j])):
                    if username in contestsData[j][k]:
                        userFound=True
                        if int(pts)>contestsData[j][k][1]:
                            contestsData[j][k][1]=int(pts)
                        break
                if userFound==False:
                    contestsData[j].append([username,int(pts)])
                break
        if contestFound==False:
            contestsData[contest]=[[username,int(pts)]]
        userFound=False
        for j in individualData:
            if j==username:
                userFound=True
                break
        if userFound==False:
            individualData[username]=0
    else:
        for i in individualData:
            for j in contestsData:
                for k in range(0,len(contestsData[j])):
                    if i==contestsData[j][k][0]:
                        individualData[i]+=contestsData[j][k][1]
                        break

        for j in contestsData:
            tempData={}
            print(f"{j}: {len(contestsData[j])} participants")
            for k in range(0,len(contestsData[j])):
                tempData[contestsData[j][k][0]]=contestsData[j][k][1]
            participantsSorted=sorted(tempData.items(),key=lambda x: x[1], reverse=True)
            participantsSorted=dict(participantsSorted)
            n=1
            for j in participantsSorted:
                print(f"{n}. {j} <::> {participantsSorted[j]}")
                n+=1

        print("Individual standings: ")
        individualDataSort = sorted(individualData.items(), key=lambda x: x[1], reverse=True)
        individualDataSort=dict(individualDataSort)
        n=1
        for j in individualDataSort:
            print(f"{n}. {j} -> {individualDataSort[j]}")
            n+=1
        break
