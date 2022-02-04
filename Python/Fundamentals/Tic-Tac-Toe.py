line1=input(); line2=input(); line3=input()
gameField=[[],[],[]]
k=0; j=0; i=0
while k<len(line1):
    num=""
    if line1[k]!=" ":
        for b in range(k,len(line1)):
            if line1[b]!=" ":
                num=line1[b]
                k+=1
            else:
                k+=1
                break
        gameField[0].append(num)
    else:
        k+=1
        break
while j<len(line2):
    num=""
    if line2[j]!=" ":
        for b in range(j,len(line2)):
            if line2[b]!=" ":
                num=line2[b]
                j+=1
            else:
                j+=1
                break
        gameField[1].append(num)
    else:
        j+=1
        break
while i<len(line3):
    num=""
    if line3[i]!=" ":
        for b in range(i,len(line3)):
            if line3[b]!=" ":
                num=line3[b]
                i+=1
            else:
                i+=1
                break
        gameField[2].append(num)
    else:
        i+=1
        break
if gameField[0][0]==gameField[0][1] and gameField[0][1]==gameField[0][2]:
    if gameField[0][0]!="0":
        winner=gameField[0][0]
    else:
        winner="Draw"
elif gameField[2][0]==gameField[2][1] and gameField[2][1]==gameField[2][2]:
    winner=gameField[2][0]
    if gameField[2][0]!="0":
        winner = gameField[2][0]
    else:
        winner="Draw"
elif gameField[0][0]==gameField[1][0] and gameField[1][0]==gameField[2][0]:
    if gameField[0][0]!="0":
        winner=gameField[0][0]
    else:
        winner="Draw"
elif gameField[0][2]==gameField[1][2] and gameField[1][2]==gameField[2][2]:
    if gameField[0][2]!="0":
        winner=gameField[0][2]
    else:
        winner="Draw"
elif gameField[1][0]==gameField[1][1] and gameField[1][1]==gameField[1][2]:
    if gameField[1][0]!="0":
        winner=gameField[1][0]
    else:
        winner="Draw"
elif gameField[0][0]==gameField[1][1] and gameField[1][1]==gameField[2][2]:
    if gameField[0][0]!="0":
        winner=gameField[0][0]
    else:
        winner="Draw"
elif gameField[0][2]==gameField[1][1] and gameField[1][1]==gameField[2][0]:
    if gameField[0][2]!="0":
        winner=gameField[0][2]
    else:
        winner="Draw"
else:
    winner="Draw"
if winner!="Draw":
    if winner=="1":
        print("First player won")
    else:
        print("Second player won")
else:
    print("Draw!")
