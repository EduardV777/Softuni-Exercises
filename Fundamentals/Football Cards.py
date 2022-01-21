cardsGiven=input()
teamA=[1,2,3,4,5,6,7,8,9,10,11]; teamB=[1,2,3,4,5,6,7,8,9,10,11]
cardsList=cardsGiven.split(" "); gameTerminated=False
for j in range(0,len(cardsList)):
    card=cardsList[j].split("-")
    if card[0]=="A":
        if int(card[1]) in teamA:
            del teamA[teamA.index(int(card[1]))]
        else:
            continue
    else:
        if int(card[1]) in teamB:
            del teamB[teamB.index(int(card[1]))]
        else:
            continue
    if len(teamA)<7 or len(teamB)<7:
        gameTerminated=True
        break
print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")
if gameTerminated==True:
    print("Game was terminated")
