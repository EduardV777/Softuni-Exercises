earnings = 0
sale = False
saleAmount = 0 #Percentage
rentCost = 10 # Percentage
holidayCost = float(input())

jigsaws = int(input())
talkingDolls = int(input())
teddyBears = int(input())
minions = int(input())
trucks = int(input())

jigsawP = 2.60
dollsP = 3.00
bearP = 4.10
minionP = 8.20
truckP = 2.00

if jigsaws + talkingDolls + teddyBears + minions + trucks >= 50:
    sale = True
    saleAmount = 25

earnings += (jigsaws * jigsawP) + (talkingDolls * dollsP) + (teddyBears * bearP) + (minions * minionP) + (trucks * truckP)

if sale == True:
    earnings -= earnings * (saleAmount / 100)

earnings -= earnings * (rentCost / 100)

if earnings >= holidayCost:
    print(f"Yes! {earnings - holidayCost:.2f} lv left.")
else:
    print(f"Not enough money! {holidayCost - earnings:.2f} lv needed.")