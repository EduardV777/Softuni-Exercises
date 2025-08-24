points = int(input())
bonusPoints = 0
totalPoints = points

if points <= 100:
    bonusPoints += 5
elif 100 < points <= 1000:
    bonusPoints += points * 0.2
else:
    bonusPoints += points * 0.1

if points % 2 == 0:
    bonusPoints += 1
elif points % 5 == 0:
    bonusPoints += 2

totalPoints += bonusPoints

print(f"{bonusPoints}\n{totalPoints}")