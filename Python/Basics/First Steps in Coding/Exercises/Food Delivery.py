chickenMenuP = 10.35
fishMenuP = 12.40
vegMenuP = 8.15
dessertP = None #20% of total cost excl. delivery
deliveryP = 2.50

chickenMenus = int(input())
fishMenus = int(input())
vegMenus = int(input())

subTotal = (chickenMenus * chickenMenuP) + (fishMenus * fishMenuP) + (vegMenus * vegMenuP)

dessertP = subTotal * 0.2

total = subTotal + dessertP + deliveryP

print(total)