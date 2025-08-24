groupBudget = int(input())
season = input()
groupSize = int(input())

costs = 0

boatRent = [3000, 4200, 2600] #spring summer/autumn winter
sales = [10, 15, 25] #[1,6] [7,11] [12># ]

evenSizeSale = 5 #pct

if season == "Spring":
    costs += boatRent[0]
elif season == "Summer" or season == "Autumn":
    costs += boatRent[1]
elif season == "Winter":
    costs += boatRent[2]


if 0 < groupSize <= 6:
    costs -= costs * (sales[0] / 100)
elif 7 <= groupSize <= 11:
    costs -= costs * (sales[1] / 100)
elif 12 <= groupSize:
    costs -= costs * (sales[2] / 100)

if season == "Spring" or season == "Winter" or season == "Summer":
    if groupSize % 2 == 0:
        costs -= costs * (evenSizeSale / 100)

if costs <= groupBudget:
    print(f"Yes! You have {groupBudget - costs:.2f} leva left.")
else:
    print(f"Not enough money! You need {costs - groupBudget:.2f} leva.")