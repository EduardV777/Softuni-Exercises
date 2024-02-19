import math
#vehicle1 [carType][yearsToPayTaxFor][kilometersTraveled]>> vehicle2 >> vehicle3
#valid types of cars: family, heavyDuty, sports

stringData = input()
totalCollected = 0
separateVehicles = stringData.split(">>")

for x in range(0, len(separateVehicles)):
    carData = separateVehicles[x].split()

    carType = carData[0]
    taxYears = int(carData[1])
    kilometersTraveled = int(carData[2])
    totalTax = 0

    if carType == "family":
        initialTax = 50

        totalTax = initialTax
        totalTax -= 5 * taxYears
        totalTax += math.floor(kilometersTraveled / 3000) * 12

    elif carType == "heavyDuty":
        initialTax = 80

        totalTax = initialTax
        totalTax -= 8 * taxYears
        totalTax += math.floor(kilometersTraveled / 9000) * 14
    elif carType == "sports":
        initialTax = 100

        totalTax = initialTax
        totalTax -= 9 * taxYears
        totalTax += math.floor(kilometersTraveled / 2000) * 18
    else:
        print("Invalid car type.")
        continue

    print(f"A {carType} car will pay {totalTax:.2f} euros in taxes.")
    totalCollected += totalTax

print(f"The National Revenue Agency will collect {totalCollected:.2f} euros in taxes.")