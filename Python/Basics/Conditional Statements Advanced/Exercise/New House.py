flowerType = input()
flowersAmount = int(input())
budget = int(input())
costs = 0
prices = [5, 3.80, 2.80, 3, 2.50] # rose dahlia tulip narcissus gladiolus

if flowerType == "Roses":
    costs = flowersAmount * prices[0]

    if flowersAmount > 80:
        costs -= costs * 0.1

elif flowerType == "Dahlias":
    costs = flowersAmount * prices[1]

    if flowersAmount > 90:
        costs -= costs * 0.15

elif flowerType == "Tulips":
    costs = flowersAmount * prices[2]

    if flowersAmount > 80:
        costs -= costs * 0.15

elif flowerType == "Narcissus":
    costs = flowersAmount * prices[3]

    if flowersAmount < 120:
        costs += costs * 0.15
elif flowerType == "Gladiolus":
    costs = flowersAmount * prices[4]

    if flowersAmount < 80:
        costs += costs * 0.2

if costs <= budget:
    print(f"Hey, you have a great garden with {flowersAmount} {flowerType} and {budget - costs:.2f} leva left.")
else:
    print(f"Not enough money, you need {costs - budget:.2f} leva more.")