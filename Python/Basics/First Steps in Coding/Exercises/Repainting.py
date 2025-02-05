protectiveCoverPerMeter = 1.50
paintPerLiter = 14.50
thinnerPerLiter = 5.00
workersPricePerHour = None # 30 percent of all materials costs

additionalPaintPct = 0.1; additionalCoverMeters = 2; envelopesPrice = 0.40

protectiveCover = int(input()) + additionalCoverMeters
paint = int(input())
thinner = int(input())
workersHours = int(input())

totalMatCosts = (protectiveCover * protectiveCoverPerMeter) + ((paint + (paint * additionalPaintPct)) * paintPerLiter) + (thinner * thinnerPerLiter) + envelopesPrice
workersCosts = (totalMatCosts * 0.3) * workersHours
totalCosts = totalMatCosts + workersCosts

print(f"{totalCosts}")