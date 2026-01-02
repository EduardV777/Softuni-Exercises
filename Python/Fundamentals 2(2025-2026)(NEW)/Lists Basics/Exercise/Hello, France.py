collection = input().split("|")
budget = float(input())

boughtItemValues = []
profit = 0
trainTicket = 150
markup = 40 #pct

#format collection list
for k in range(0, len(collection)):
    type = collection[k].split("->")[0]
    price = float(collection[k].split("->")[1])

    collection[k] = [type, price]

# clothes 50.00 shoes 35.00 accessories 20.50 MAX PRICES

for k in range(0, len(collection)):
    if collection[k][0] == "Clothes":
        if collection[k][1] <= 50.00:
            if budget >= collection[k][1]:
                budget -= collection[k][1]
                boughtItemValues.append(collection[k][1])

    elif collection[k][0] == "Shoes":
        if collection[k][1] <= 35.00:
            if budget >= collection[k][1]:
                budget -= collection[k][1]
                boughtItemValues.append(collection[k][1])

    elif collection[k][0] == "Accessories":
        if collection[k][1] <= 20.50:
            if budget >= collection[k][1]:
                budget -= collection[k][1]
                boughtItemValues.append(collection[k][1])


#calculate budget with profit by selling bought items with 40% markup
for k in range(0, len(boughtItemValues)):
    profit += boughtItemValues[k] * 0.4
    boughtItemValues[k] = round(boughtItemValues[k] + (boughtItemValues[k] * 0.4), 2)
    budget += boughtItemValues[k]
    boughtItemValues[k] = str(boughtItemValues[k])

print(" ".join(boughtItemValues))
print(f"Profit: {profit:.2f}")


if budget >= trainTicket:
    print("Hello, France!")
else:
    print("Not enough money.")
