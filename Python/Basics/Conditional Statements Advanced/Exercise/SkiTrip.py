days = int(input()) - 1
typeOfStay = input() #"room for one person", "apartment" или "president apartment"
estimate = input() # positive negative
total = 0
# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка

oneRoom = 18
apartment = 25
presidentAp = 35

if typeOfStay == "room for one person":
    total = days * oneRoom
elif typeOfStay == "apartment":
    total = days * apartment
elif typeOfStay == "president apartment":
    total = days * presidentAp

if typeOfStay == "apartment":
    if days < 10:
        total -= total * 0.3
    elif 10 <= days <= 15:
        total -= total * 0.35
    elif days > 15:
        total -= total * 0.5
elif typeOfStay == "president apartment":
    if days < 10:
        total -= total * 0.1
    elif 10 <= days <= 15:
        total -= total * 0.15
    elif days > 15:
        total -= total * 0.2


if estimate == "positive":
    total += total * 0.25
elif estimate == "negative":
    total -= total * 0.1

print(f"{total:.2f}")


