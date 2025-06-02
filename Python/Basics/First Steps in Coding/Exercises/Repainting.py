nylonSqMPrice = 1.50
paintLPrice = 14.50
paintThinnerLPrice = 5

paintLAddPct = 10
nylonAddSqUnits = 2
bagsExpenses = 0.40

nylonSqMeters = int(input())
paintLiters = int(input())
thinnerLiters = int(input())
buildersWorkHours = int(input())

total = ((nylonSqMeters + nylonAddSqUnits) * nylonSqMPrice) + ((paintLiters + (paintLiters * paintLAddPct / 100)) * paintLPrice) + (thinnerLiters * paintThinnerLPrice) \
    + bagsExpenses

workHourExpense = total * 0.30

total += workHourExpense * buildersWorkHours

print(f"{total}")