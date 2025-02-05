SqMeterPrice = 7.61
TotalSale = 0.18

SqMeters = float(input())

subTotal = SqMeters * SqMeterPrice
sale = subTotal * TotalSale
total = subTotal - sale

print(f"The final price is: {total} lv.")
print(f"The discount is: {sale} lv.")