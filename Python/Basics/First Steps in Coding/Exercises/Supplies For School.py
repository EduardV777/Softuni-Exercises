penQty = int(input())
markerQty = int(input())
detergentLitres = int(input())
salePct = int(input())


penPrice = 5.80
markerPrice = 7.20
detergentPriceL = 1.20

total = (penQty * penPrice) + (markerQty * markerPrice) + (detergentLitres * detergentPriceL)
discount = (salePct / 100) * total

print(total - discount)
