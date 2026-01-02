import re
n=int(input())
for k in range(0,n):
    data=input()
    findValidData=re.compile(r"(?P<Boss>\|[A-Z]{4,}\|):(?P<Title>#[A-Za-z]+\s[A-Za-z]+#)")
    occurrences=findValidData.findall(data)
    if len(occurrences)==0:
        print("Access denied!")
    else:
        bossName=occurrences[0][0].split("|")
        bossName=bossName[1]
        title=occurrences[0][1].split("#")
        title=title[1]
        Strength=len(bossName)
        Armor=occurrences[0][1].split("#")
        Armor=Armor[1]
        Armor=len(Armor)
        print(f"{bossName}, The {title}\n>> Strength: {Strength}\n>> Armor: {Armor}")
