str=input()
sentOffPlayers=[]
k=0; teamA=11; teamB=11; gameTerminated=False
while k<len(str):
    ignore = False; num=""
    if not str[k]==" ":
        if str[k]=="A":
            for i in range(k+2,len(str)):
                if str[i]==" ":
                    break
                else:
                    num+=str[i]
            num+="A"
            #has player already been sent off?
            for j in range(0,len(sentOffPlayers)):
                if num==sentOffPlayers[j]:
                    ignore=True
                    break
            if ignore==True:
                k+=4
            else:
                teamA-=1
                sentOffPlayers.append(num)
                k+=4
        elif str[k]=="B":
            for i in range(k+2,len(str)):
                if str[i]==" ":
                    break
                else:
                    num+=str[i]
            num+="B"
            #has player already been sent off?
            for j in range(0,len(sentOffPlayers)):
                if num==sentOffPlayers[j]:
                    ignore=True
            if ignore==True:
                k+=4
            else:
                teamB-=1
                sentOffPlayers.append(num)
                k+=4
    else:
        k+=1
    if teamA<7 or teamB<7:
        gameTerminated=True
        break
if gameTerminated==True:
    print(f"Team A - {teamA}; Team B - {teamB}")
    print("Game was terminated")
else:
    print(f"Team A - {teamA}; Team B - {teamB}")
