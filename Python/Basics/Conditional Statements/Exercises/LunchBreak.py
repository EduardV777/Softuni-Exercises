from math import ceil

seriesName = input()
episodeLength = int(input())
restLength = int(input())


lunchTime = restLength / 8
relaxTime = restLength / 4

restLength -= lunchTime + relaxTime

if restLength >= episodeLength:
    print(f"You have enough time to watch {seriesName} and left with {ceil(restLength - episodeLength)} minutes free time.")
else:
    print(f"You don't have enough time to watch {seriesName}, you need {ceil(episodeLength - restLength)} more minutes.")