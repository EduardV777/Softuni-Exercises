n = int(input())

tankL = 0
capL = 255

while n:
    liters = int(input())

    if liters + tankL <= capL:
        tankL += liters
    else:
        print("Insufficient capacity!")

    n -= 1

print(tankL)