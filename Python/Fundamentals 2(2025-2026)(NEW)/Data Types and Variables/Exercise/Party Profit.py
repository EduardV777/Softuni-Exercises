from math import floor

groupSize = int(input())
daysAdventure = int(input())
day = 1
coins = 0

while day <= daysAdventure:
    if day % 10 == 0: # every 10th day 2 companions leave the group at the start of the day
        groupSize -= 2
    if day % 15 == 0: # every 15th day 5 companions join the group
        groupSize += 5

    spending = 0
    coins += 50

    spending += 2 * groupSize # food per companion each day

    if day % 3 == 0:    #motivational party organized
        spending += 3 * groupSize #for drinking water

    if day % 5 == 0: # slaying boss monster
        coins += 20 * groupSize

        if day % 3 == 0: # if there is also a motivational party that day, that will lead to additional spending
            spending += 2 * groupSize

    coins -= spending
    day += 1

print(f"{groupSize} companions received {floor(coins / groupSize)} coins each.")