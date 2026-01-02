#default values (HEALTH 250, DMG 45, ARMOR 10)
n=int(input())
dragons={}
for k in range(0,n):
    dragonStats=input()
    statsList=dragonStats.split(" ")
    type=statsList[0]; name=statsList[1]; dmg=statsList[2]; hp=statsList[3]; armor=statsList[4]

    #if any int value is null
    if dmg=="null":
        dmg=45
    elif hp=="null":
        hp=250
    elif armor=="null":
        armor=10
    dmg=int(dmg); hp=int(hp); armor=int(armor)

    typeExists=False; dragonExists=False
    for j in dragons:
        if j==type:
            typeExists=True
            for k in range(0,len(dragons[j])):
                if name==dragons[j][k][0]:
                    dragonExists=True
                    if j!=type:
                        dragonExists=False
                    else:
                        dragons[j][k][1]=dmg; dragons[j][k][2]=hp; dragons[j][k][3]=armor
                    break
            break
    if typeExists==False:
        dragons[type]=[[name,dmg,hp,armor]]
    elif dragonExists==False:
        dragons[type].append([name,dmg,hp,armor])

for j in dragons:
    dragons[j].sort()
    avgDmg=0; avgHP=0; avgArmor=0
    for k in range(0,len(dragons[j])):
        avgDmg+=dragons[j][k][1]
        avgHP+=dragons[j][k][2]
        avgArmor+=dragons[j][k][3]
    avgDmg/=len(dragons[j])
    avgHP/=len(dragons[j])
    avgArmor/=len(dragons[j])
    print(f"{j}::({avgDmg:.2f}/{avgHP:.2f}/{avgArmor:.2f})")
    for k in range(0,len(dragons[j])):
        print(f"-{dragons[j][k][0]} -> damage: {dragons[j][k][1]}, health: {dragons[j][k][2]}, armor: {dragons[j][k][3]}")
