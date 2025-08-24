from math import floor

record = float(input()) #seconds
distance = float(input()) #meters
timePerMeter = float(input()) #seconds
slowDowns = floor(distance / 15)


competitorTime = distance * timePerMeter + (slowDowns * 12.5)

if competitorTime < record:
    print(f"Yes, he succeeded! The new world record is {competitorTime:.2f} seconds.")
else:
    print(f"No, he failed! He was {competitorTime - record:.2f} seconds slower.")