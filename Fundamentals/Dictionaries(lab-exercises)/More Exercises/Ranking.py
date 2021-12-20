contests={}
participantsData={}
while True:
    command=input()
    if ":" in command:
        contestData=command.split(":")
        contest=contestData[0]; passw=contestData[1]
        contestFound=False
        for j in contests:
            if contest==j:
                contestFound=True
                break
        if contestFound==False:
            contests[contest]=passw
    elif command=="end of contests":
        break
while True:
    command=input()
    if "=>" in command:
        rankingData=command.split("=>")
        contestFound=False; passCorrect=False
        for j in contests:
            if rankingData[0]==j:
                contestFound=True
                if contests[j]==rankingData[1]:
                    passCorrect=True
                    break
                else:
                    break
        if contestFound==False:
            pass
        elif passCorrect==False:
            pass
        if contestFound==True and passCorrect==True:
            participantFound=False; participantsContestFound=False
            for j in participantsData:
                if j==rankingData[2]:
                    participantFound=True
                    for k in range(0,len(participantsData[j])):
                        participantContests=participantsData[j][k].split("-")
                        contestID=participantContests[0]
                        if contestID==rankingData[0]:
                            ind=k
                            participantsContestFound=True
                            break
                    break
            if participantFound==False and participantsContestFound==False:
                participantsData[rankingData[2]]=[f"{rankingData[0]}-{rankingData[3]}"]
            elif participantFound==True and participantsContestFound==False:
                participantsData[rankingData[2]].append(f"{rankingData[0]}-{rankingData[3]}")
            elif participantFound==True and participantsContestFound==True:
                if rankingData[3]>participantsData[rankingData[2]][1]:
                    participantsData[rankingData[2]][ind]=f"{rankingData[0]}-{rankingData[3]}"
    elif command=="end of submissions":
        break

for j in participantsData:
    totalPts=0
    for k in range(0,len(participantsData[j])):
        pts=participantsData[j][k].split("-"); pts=int(pts[1])
        totalPts+=pts
    participantsData[j].insert(0,totalPts)
orderByTotalPts=sorted(participantsData.items(),key=lambda x:x[1][0],reverse=True)
orderByTotalPts=dict(orderByTotalPts)
#print(orderByTotalPts)
i=0
for j in orderByTotalPts:
    if i==0:
        print(f"Best candidate is {j} with total {orderByTotalPts[j][0]} points.")
        print("Ranking:")
        orderByName=sorted(orderByTotalPts.items(),key=lambda x:x[0])
        orderByName=dict(orderByName)
        i+=1
    for h in orderByName:
        print(f"{h}")
        contestsAndPoints=[]
        for k in range(1,len(orderByName[h])):
            orderByName[h][0]=str(orderByName[h][0])
            data=orderByName[h][k].split("-")
            contestsAndPoints.append((data[0],int(data[1])))
        contestsAndPoints=dict(contestsAndPoints)
        contestsAndPoints=sorted(contestsAndPoints.items(),key=lambda x: x[1],reverse=True)
        contestsAndPoints=dict(contestsAndPoints)
        for k in contestsAndPoints:
            print(f"#  {k} -> {contestsAndPoints[k]}")
    break
