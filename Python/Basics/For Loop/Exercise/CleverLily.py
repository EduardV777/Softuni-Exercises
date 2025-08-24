age = int(input())
washingMachinePrice = float(input())
pricePerToy = int(input())

savedMoney = 0
bDayMoney = 10
toys = 0

for k in range(1,age + 1):
    if k % 2 == 0:
        savedMoney += bDayMoney
        bDayMoney += 10
    else:
        toys += 1

savedMoney -= ((bDayMoney - 10) / 10) * 1
savedMoney += toys * pricePerToy

if savedMoney >= washingMachinePrice:
    print(f"Yes! {savedMoney - washingMachinePrice:.2f}" )
else:
    print(f"No! {washingMachinePrice - savedMoney:.2f}" )