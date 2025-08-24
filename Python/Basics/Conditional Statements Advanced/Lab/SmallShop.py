cost = 0.00

prod = input()
city = input()
qty = float(input())

prices = [[0.50, 0.80, 1.20, 1.45, 1.60], [0.40,0.70,1.15,1.30,1.50], [0.45,0.70,1.10,1.35,1.55]] #coffee, water, beer, sweets, peanuts

if city == "Sofia":
    if prod == "coffee":
        cost += prices[0][0] * qty
    elif prod == "water":
        cost += prices[0][1] * qty
    elif prod == "beer":
        cost += prices[0][2] * qty
    elif prod == "sweets":
        cost += prices[0][3] * qty
    elif prod == "peanuts":
        cost += prices[0][4] * qty


elif city == "Plovdiv":
    if prod == "coffee":
        cost += prices[1][0] * qty
    elif prod == "water":
        cost += prices[1][1] * qty
    elif prod == "beer":
        cost += prices[1][2] * qty
    elif prod == "sweets":
        cost += prices[1][3] * qty
    elif prod == "peanuts":
        cost += prices[1][4] * qty

elif city == "Varna":
    if prod == "coffee":
        cost += prices[2][0] * qty
    elif prod == "water":
        cost += prices[2][1] * qty
    elif prod == "beer":
        cost += prices[2][2] * qty
    elif prod == "sweets":
        cost += prices[2][3] * qty
    elif prod == "peanuts":
        cost += prices[2][4] * qty

print(cost)