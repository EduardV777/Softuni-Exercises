initPoints = int(input())

bonusPoints = 0
totalPoints = initPoints

if totalPoints <= 100:
    bonusPoints = 5

elif 100 < totalPoints <= 1000:
    bonusPoints += initPoints * 0.2

else:
    bonusPoints += initPoints * 0.1

if totalPoints % 2 == 0:
    bonusPoints += 1

if totalPoints % 10 == 5:
    bonusPoints += 2

totalPoints += bonusPoints

print(bonusPoints)
print(totalPoints)