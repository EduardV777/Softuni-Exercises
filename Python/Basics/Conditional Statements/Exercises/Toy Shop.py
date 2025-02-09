puzzlePrice = 2.60
dollPrice = 3
teddyPrice = 4.10
minionPrice = 8.20
truckPrice = 2

vacationCost = float(input())
puzzles = int(input())
dolls = int(input())
teddyBears = int(input())
minions = int(input())
trucks = int(input())

allToys = puzzles + dolls + teddyBears + minions + trucks
subTotal = (puzzles * puzzlePrice) + (dolls * dollPrice) + (teddyBears * teddyPrice) + (minions * minionPrice) + (trucks * truckPrice)

if allToys >= 50:
    subTotal -= subTotal * 0.25

#rent
subTotal -= subTotal * 0.1

if subTotal >= vacationCost:
    print(f"Yes! {subTotal - vacationCost:.2f} lv left.")
else:
    print(f"Not enough money! {vacationCost - subTotal:.2f} lv needed.")