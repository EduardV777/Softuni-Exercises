decorationCost = 10 #percentage of budget
sale = False
saleAmount = 0
costs = 0

budget = float(input())
extras = int(input())
outfitCostPerExtra = float(input())

if extras > 150:
    sale = True
    saleAmount = 10

costs += (budget * (decorationCost / 100))

if sale == True:
    costs += (outfitCostPerExtra * extras) - ((outfitCostPerExtra * extras) * (saleAmount / 100))
else:
    costs += outfitCostPerExtra * extras

if costs <= budget:
    print(f"Action!\nWingard starts filming with {budget - costs:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {costs - budget:.2f} leva more.")