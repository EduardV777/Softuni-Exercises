n=int(input())
plants={}
#on the next n lines
#information about plants in the following format "{plant}<->{rarity}"
for k in range(0,n):
    plantData=input()
    plantData=plantData.split("<->")
    plantName=plantData[0]; plantRarity=plantData[1]
    plants[plantName]=[plantRarity,[]]
while True:
    command=input()
    if command!="Exhibition":
        if 'Rate' in command:
            command=command.split(": ")
            plantData=command[1]
            plantData=plantData.split(" - ")
            if plantData[0] in plants:
                plants[plantData[0]][1].append(int(plantData[1]))
            else:
                print("error")
        elif 'Update' in command:
            command=command.split(": ")
            plantData=command[1]
            plantData=plantData.split(" - ")
            if plantData[0] in plants:
                plants[plantData[0]][0]=int(plantData[1])
            else:
                print("error")
        elif 'Reset' in command:
            command=command.split(": ")
            if command[1] in plants:
                plants[command[1]][1]=[]
            else:
                print("error")
    else:
        print("Plants for the exhibition:")
        for plant in plants:
            totalRating=0; ratings=len(plants[plant][1])
            for k in range(0,len(plants[plant][1])):
                totalRating+=plants[plant][1][k]
            if ratings!=0:
                totalRating/=ratings
            plants[plant][1]=totalRating
            print(f"- {plant}; Rarity: {plants[plant][0]}; Rating: {plants[plant][1]:.2f}")
        break
