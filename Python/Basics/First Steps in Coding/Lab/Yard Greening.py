squareMeters = float(input())

SqMPrice = 7.61
totalSale = 18

total = squareMeters * SqMPrice
discount = total * (totalSale / 100)

total -= discount

print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")
