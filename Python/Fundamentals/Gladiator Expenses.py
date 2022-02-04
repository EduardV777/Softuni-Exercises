lostFights=int(input()); helmetPrice=float(input()); swordPrice=float(input()); shieldPrice=float(input()); armorPrice=float(input())
every2ndGame=2; every3rdGame=3; brokenShieldTimes=0; expenses=0
brokenHelmet=False; swordBroken=False
for k in range(1,lostFights+1):
    if k==every2ndGame:
        brokenHelmet=True
        expenses+=helmetPrice
        every2ndGame+=2
    if k==every3rdGame:
        swordBroken=True
        expenses+=swordPrice
        if brokenHelmet==True:
            expenses+=shieldPrice
            brokenShieldTimes+=1
            if brokenShieldTimes%2==0:
                expenses+=armorPrice
        every3rdGame+=3
    brokenHelmet = False; swordBroken = False
print(f"Gladiator expenses: {expenses:.2f} aureus")
