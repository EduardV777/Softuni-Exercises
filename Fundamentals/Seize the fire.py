firesNCells=input(); water=int(input())
firesCells=[]; cellExtinguished=[]
effort=0; totalExtinguished=0
k=0
while k<(len(firesNCells)):
    cellN=""; fireType="";
    if firesNCells[k]!=" " and firesNCells[k]!="#" and firesNCells[k]!="=":
        if firesNCells[k].isalpha()==True:
            for j in range(k,len(firesNCells)):
                if firesNCells[j]!=" ":
                    fireType+=firesNCells[j]
                    k+=1
                else:
                    k+=1
                    break
            firesCells.append([fireType])
        elif firesNCells[k].isdigit()==True:
            for j in range(k,len(firesNCells)):
                if firesNCells[j]!=" " and firesNCells[j]!="#":
                    cellN+=firesNCells[j]
                    k+=1
                else:
                    k+=1
                    break
            firesCells[len(firesCells)-1].append(cellN)
    else:
        k+=1
#print(firesCells)
for k in range(0,len(firesCells)):
    for j in range(0,1):
        if firesCells[k][j]=="High":
            if 81<=int(firesCells[k][j+1])<=125:
                if water>=int(firesCells[k][j+1]):
                    water-=int(firesCells[k][j+1])
                    totalExtinguished+=int(firesCells[k][j+1])
                    effort+=int(firesCells[k][j+1])*0.25
                    cellExtinguished.append(firesCells[k][j+1])
                else:
                    break
        elif firesCells[k][j]=="Medium":
            if 51<=int(firesCells[k][j+1])<=80:
                if water>=int(firesCells[k][j+1]):
                    water-=int(firesCells[k][j+1])
                    totalExtinguished += int(firesCells[k][j + 1])
                    effort += int(firesCells[k][j + 1]) * 0.25
                    cellExtinguished.append(firesCells[k][j+1])
                else:
                    break
        elif firesCells[k][j]=="Low":
            if 10 <= int(firesCells[k][j+1]) <= 50:
                if water>=int(firesCells[k][j+1]):
                    water-=int(firesCells[k][j+1])
                    totalExtinguished += int(firesCells[k][j + 1])
                    effort += int(firesCells[k][j + 1]) * 0.25
                    cellExtinguished.append(firesCells[k][j+1])
                else:
                    break
print("Cells:")
for k in range(0,len(cellExtinguished)):
    print(f"- {cellExtinguished[k]}")
print(f"Effort: {effort:.2f}\nTotal Fire: {totalExtinguished}")
