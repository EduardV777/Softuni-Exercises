n=int(input())
field=[]; allAttacks=[]
for k in range(0,n):
    field.append(list())
k=0; shipsDestroyed=0
while k<n:
    rowField=input()
    i=0
    while i<len(rowField):
        ship=""
        if rowField[i]!=" ":
            for j in range(i,len(rowField)):
                if rowField[j]!=" ":
                    ship+=rowField[j]
                    i+=1
                else:
                    break
            ship=int(ship)
            field[k].append(ship)
        else:
            i+=1
    k+=1
attacks=input()
k=0
while k<len(attacks):
    currentAttack=""
    if attacks[k]!=" ":
        for j in range(k,len(attacks)):
            if attacks[j]!=" ":
                currentAttack+=attacks[j]
                k+=1
            else:
                break
        allAttacks.append(currentAttack)
    else:
        k+=1

for k in range(0,len(allAttacks)):
    row=int(allAttacks[k][0]); col=int(allAttacks[k][2])
    field[row][col]-=1
    if field[row][col]==0:
        shipsDestroyed+=1
print(shipsDestroyed)
