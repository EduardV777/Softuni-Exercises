penPacks = int(input())
markerPacks = int(input())
detergentLiters = int(input())
salePct = int(input())

penPackP = 5.80
markerPackP = 7.20
detergentLPrice = 1.20


total = (penPacks * penPackP) + (markerPacks * markerPackP) + (detergentLiters * detergentLPrice)
total -= total * (salePct / 100)

print(total)