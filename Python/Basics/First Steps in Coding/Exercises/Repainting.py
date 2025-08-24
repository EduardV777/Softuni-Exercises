coverSqP = 1.50
paintLPrice = 14.50
thinnerLPrice = 5
bagsP = 0.40
workersHourlyPay = None # 30% of all materials cost

#10% additional paint
addPaint = 0.1
#2 additional sq meters of cover
addCover = 2

cover = int(input()) + addCover
paint = int(input())
thinner = int(input())
hours = int(input())

paint += paint * addPaint

materialsCost = bagsP + (cover * coverSqP) + (paint * paintLPrice) + (thinner * thinnerLPrice)

workersHourlyPay = materialsCost * 0.3

totalCost =  materialsCost + (hours * workersHourlyPay)

print(totalCost)