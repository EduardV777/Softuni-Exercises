# 	W - ако е победител получава 2000 точки
# 	F - ако е финалист получава 1200 точки
# 	SF - ако е полуфиналист получава 720 точки
from math import floor
tournaments = int(input())
totalPts = int(input())

winPcts = 0
totalPlayed = 0
pointsWon = 0
avgPts = 0

for k in range(0, tournaments):
    stage = input()

    if stage == "W":
        totalPts += 2000
        pointsWon += 2000
        winPcts += 1
    elif stage == "F":
        totalPts += 1200
        pointsWon += 1200
    elif stage == "SF":
        totalPts += 720
        pointsWon += 720

    totalPlayed += 1

winPcts = (winPcts / totalPlayed) * 100
avgPts = floor(pointsWon / totalPlayed)

print(f"Final points: {totalPts}\nAverage points: {avgPts}\n{winPcts:.2f}%")