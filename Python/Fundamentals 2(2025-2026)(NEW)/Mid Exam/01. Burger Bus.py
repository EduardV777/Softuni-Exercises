citiesCount = int(input())
citiesList = list()
totalProfit = 0

for x in range(0, citiesCount):
    cityName = input()
    ownerIncome = float(input())
    ownerExpenses = float(input())

    if (x + 1) % 5 == 0:
        ownerIncome -= ownerIncome * 0.1
    elif (x + 1) % 3 == 0:
        ownerExpenses += ownerExpenses * 0.5


    cleanProfit = ownerIncome - ownerExpenses
    totalProfit += cleanProfit
    print(f"In {cityName} Burger Bus earned {cleanProfit:.2f} leva.")

    citiesList.append(list([cityName, cleanProfit, ownerExpenses]))

print(f"Burger Bus total profit: {totalProfit:.2f} leva.")