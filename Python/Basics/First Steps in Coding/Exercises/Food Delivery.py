chickenMenuPrice = 10.35
fishMenuPrice = 12.40
vegMenuPrice = 8.15

deliveryPrice = 2.50

chickenMenuQty = int(input())
fishMenuQty = int(input())
vegMenuQty = int(input())

total = (chickenMenuQty * chickenMenuPrice) + (fishMenuQty * fishMenuPrice) + (vegMenuQty * vegMenuPrice)

dessertPrice = total * 0.20

total += dessertPrice + deliveryPrice

print(f"{total}")
