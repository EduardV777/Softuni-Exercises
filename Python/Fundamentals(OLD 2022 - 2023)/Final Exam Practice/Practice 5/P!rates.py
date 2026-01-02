targetCities={}

def ActionOnTargets():
    while True:
        command=input()
        if command!="End":
            if "Plunder" in command:
                command=command.split("=>")
                town=command[1]; peopleKilled=int(command[2]); goldStolen=int(command[3])
                targetCities[town][0]-=peopleKilled; targetCities[town][1]-=goldStolen
                print(f"{town} plundered! {goldStolen} gold stolen, {peopleKilled} citizens killed.")
                if targetCities[town][0]<=0 or targetCities[town][1]<=0:
                    del targetCities[town]
                    print(f"{town} has been wiped off the map!")
            elif "Prosper" in command:
                command=command.split("=>")
                town=command[1]; gold=int(command[2])
                if not gold<0:
                    targetCities[town][1]+=gold
                    print(f"{gold} gold added to the city treasury. {town} now has {targetCities[town][1]} gold.")
                else:
                    print("Gold added cannot be a negative number!")
        else:
            break


while True:
    cityData=input()
    if cityData!="Sail":
        cityData=cityData.split("||")
        cityName=cityData[0]; population=int(cityData[1]); gold=int(cityData[2])
        if not cityName in targetCities:
            targetCities[cityName]=[population, gold]
        else:
            targetCities[cityName][0]+=population
            targetCities[cityName][1]+=gold
    else:
        ActionOnTargets()
        break
if len(targetCities)>0:
    print(f"Ahoy, Captain! There are {len(targetCities)} wealthy settlements to go to:")
    for j in targetCities:
        print(f"{j} -> Population: {targetCities[j][0]} citizens, Gold: {targetCities[j][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
