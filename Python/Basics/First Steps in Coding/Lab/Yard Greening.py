squareMeters = float(input())

sqMeterP = 7.61
#18% sale of total
totalCost = squareMeters * sqMeterP
saleAmount = totalCost * 0.18



print(f"The final price is: {totalCost - saleAmount} lv.\nThe discount is: {saleAmount} lv.")
