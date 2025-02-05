penPackPrice = 5.80
markerPackPrice = 7.20
detergentLiterPrice = 1.20


penPacks = int(input())
markerPacks = int(input())
detergent = int(input())
sale = int(input()) / 100

subTotal = (penPacks * penPackPrice) + (markerPacks * markerPackPrice) + (detergent * detergentLiterPrice)
total = subTotal - (subTotal * sale)

print(total)