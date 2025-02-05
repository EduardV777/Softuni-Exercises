chickenMenuPrice = 10.35
fishMenuPrice = 12.40
vegMenuPrice = 8.15
deliveryPrice = 2.50
dessertPrice = None # 20% total Sum delivery excluded

chickenMenus = int(input())
fishMenus = int(input())
vegMenus = int(input())

subTotal = (chickenMenus * chickenMenuPrice) + (fishMenus * fishMenuPrice) + (vegMenus * vegMenuPrice)
dessertPrice = subTotal * 0.2; subTotal += dessertPrice

total = subTotal + deliveryPrice

print(f"{total:.2f}")