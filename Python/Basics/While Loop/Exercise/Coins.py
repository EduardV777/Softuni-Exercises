from math import floor

change = float(input())
coins = 0

whole = floor(change)
remaining = (round((change - whole) * 100,2))


whole /= 2
while floor(whole) > 0:
    coins += 1
    whole -= 1

if whole != 0:
    coins += 1
    whole -= 0.5

while remaining != 0:
    if remaining >= 50:
        remaining -= 50
    elif remaining >= 20:
        remaining -= 20
    elif remaining >= 10:
        remaining -= 10
    elif remaining >= 5:
        remaining -= 5
    elif remaining >= 2:
        remaining -= 2
    elif remaining >= 1:
        remaining -= 1

    coins += 1

print(coins)



