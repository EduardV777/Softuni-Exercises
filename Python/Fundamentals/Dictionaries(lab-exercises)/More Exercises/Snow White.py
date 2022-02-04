dwarves={}
while True:
    command=input()
    if command!="Once upon a time":
        dwarfChar=command.split(" <:> ")
        name=dwarfChar[0]; hatCol=dwarfChar[1]; physics=int(dwarfChar[2])
        dwarfExists=False; colorExists=False
        for j in dwarves:
            if j==hatCol:
                colorExists=True
                for k in range(0,len(dwarves[j])):
                    if dwarves[j][k][0]==name:
                        dwarfExists=True
                        if dwarves[j][k][1]<physics:
                            dwarves[j][k][1]=physics
                            break
                break
        if colorExists==False:
            dwarves[hatCol]=[[name,physics]]
        elif dwarfExists==False:
            dwarves[hatCol].append([name,physics])
    else:
        dwarves=sorted(dwarves.items(),key=lambda x: x[1][0][1],reverse=True)
        dwarves=dict(dwarves)
        for j in dwarves:
            dwarves[j].append(len(dwarves[j]))
        dwarves=sorted(dwarves.items(),key=lambda x: x[1][-1],reverse=True)
        dwarves=dict(dwarves)
        for j in dwarves:
            del dwarves[j][-1]
            for k in range(0,len(dwarves[j])):
                print(f"({j}) {dwarves[j][k][0]} <-> {dwarves[j][k][1]}")
        break
