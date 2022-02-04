playerPool={}
while True:
    playerData=input()
    if playerData!="Season end":
        if not "vs" in playerData:
            data=playerData.split(" -> ")
            playerName=data[0]; playerPos=data[1]; playerSkill=int(data[2])
            playerFound=False
            for j in playerPool:
                if j==playerName:
                    playerFound=True; positionExists=False
                    for k in range(0,len(playerPool[j])):
                        if playerPos in playerPool[j][k]:
                            positionExists=True
                            ind=k
                    if positionExists==True:
                        if playerPool[j][ind][1]<playerSkill:
                            playerPool[j][ind][1]=playerSkill
                            break
                    else:
                        playerPool[j].append([playerPos,playerSkill])
                    break
            if playerFound==False:
                playerPool[playerName]=[[playerPos,playerSkill]]
        else:
            players=playerData.split(" vs ")
            player1=players[0]; player2=players[1]
            if player1 in playerPool and player2 in playerPool:
                positionsLen=len(playerPool[player1]); positionsLen2=len(playerPool[player2])
                if playerPool[player1][positionsLen-1][0]==playerPool[player2][positionsLen2-1][0]:
                    if playerPool[player1][positionsLen-1][1]>playerPool[player2][positionsLen2-1][1]:
                        #player1 wins
                        del playerPool[player2]
                    elif playerPool[player1][positionsLen-1][1]==playerPool[player2][positionsLen2-1][1]:
                        #duel is tie
                        pass
                    else:
                        #player2 wins
                        del playerPool[player1]
    else:
        tempData={}
        for j in playerPool:
            totalSkill = 0
            for k in range(0, len(playerPool[j])):
                totalSkill += playerPool[j][k][1]
            tempData[j]=totalSkill
        tempDataSort=sorted(tempData.items(),key=lambda x: x[1], reverse=True)
        tempDataSort=dict(tempDataSort)
        for j in tempDataSort:
            tempSkillPosData={}
            print(f"{j}: {tempDataSort[j]} skill")
            posAndSkills=playerPool[j]
            for k in range(0,len(posAndSkills)):
                pos=posAndSkills[k][0]; skill=posAndSkills[k][1]
                tempSkillPosData[pos]=skill
            tempSkillPosData=sorted(tempSkillPosData.items(),key=lambda x: x[1], reverse=True)
            tempSkillPosData=dict(tempSkillPosData)
            for j in tempSkillPosData:
                print(f"- {j} <::> {tempSkillPosData[j]}")
        break
