#high 81-125    medium 51-80    low 1-50
fireCells=input()
fireCells=fireCells.split("#"); firesPutOut=[]
totalFire=0
for k in range(0,len(fireCells)):
    fireCells[k]=fireCells[k].split(" = ")
waterAmount=int(input())
effort=0

for k in range(0,len(fireCells)):
    if fireCells[k][0]=="High":
        if 81<=int(fireCells[k][1])<=125:
            if waterAmount>=int(fireCells[k][1]):
                effort+=int(fireCells[k][1])*0.25; totalFire+=int(fireCells[k][1])
                waterAmount-=int(fireCells[k][1])
                firesPutOut.append(fireCells[k][1])
            else:
                continue
    elif fireCells[k][0]=="Medium":
        if 51<=int(fireCells[k][1])<=80:
            if waterAmount>=int(fireCells[k][1]):
                effort += int(fireCells[k][1]) * 0.25; totalFire+=int(fireCells[k][1])
                waterAmount -= int(fireCells[k][1])
                firesPutOut.append(fireCells[k][1])
            else:
                continue
    elif fireCells[k][0]=="Low":
        if 1<=int(fireCells[k][1])<=50:
            if waterAmount>=int(fireCells[k][1]):
                effort += int(fireCells[k][1]) * 0.25; totalFire+=int(fireCells[k][1])
                waterAmount -= int(fireCells[k][1])
                firesPutOut.append(fireCells[k][1])
            else:
                continue
print(f"Cells:")
for k in range(0,len(firesPutOut)):
    print(f" - {firesPutOut[k]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {totalFire}")
