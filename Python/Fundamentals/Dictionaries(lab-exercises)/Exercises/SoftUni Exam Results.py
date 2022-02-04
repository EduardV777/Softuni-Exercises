courseParticipants={}
courseLanguages={}
while True:
    command=input()
    if "-" in command and not "banned" in command:
        participantData=command.split("-")
        username=participantData[0]; lang=participantData[1]; pts=participantData[2]
        nameFound=False; languageFound=False
        for j in courseLanguages:
            if j==lang:
                languageFound=True
                courseLanguages[j]+=1
                break
        if languageFound==False:
            courseLanguages[lang]=1
        for j in courseParticipants:
            if j==username:
                nameFound=True
                if courseParticipants[j][1]<pts:
                    courseParticipants[j][1]=pts
                    break
                else:
                    break
        if nameFound==False:
            courseParticipants[username]=[lang,pts]
    elif "-" in command and "banned" in command:
        participantBan=command.split("-")
        username=participantBan[0]
        for j in courseParticipants:
            if j==username:
                del courseParticipants[j]
                break
    elif command=="exam finished":
        orderBySubs = sorted(courseLanguages.items(), key=lambda x: x[1], reverse=True)
        orderBySubs = dict(orderBySubs)
        orderDescByPts=sorted(courseParticipants.items(),key=lambda x: x[1][1], reverse=True)
        orderDescByPts=dict(orderDescByPts)
        print("Results:")
        for j in orderDescByPts:
            print(f"{j} | {orderDescByPts[j][1]}")
        print("Submissions:")
        for j in orderBySubs:
            print(f"{j} - {orderBySubs[j]}")
        break
