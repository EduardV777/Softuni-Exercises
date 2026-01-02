lostFights = int(input())

helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

helmetStatus = True
swordStatus = True
shieldStatus = True
armorStatus = True

n = 1
t = 0 #tracks how many times the shield was broken, resets at 2
expenses = 0

while n <= lostFights:
    if n % 2 == 0:
        helmetStatus = False
    if n % 3 == 0:
        swordStatus = False

    if n % 2 == 0 and n % 3 == 0: # if helmet and sword are broken in the same fight shield also breaks
        shieldStatus = False
        t += 1

    if t == 2:
        t = 0
        armorStatus = False

    #Repairs
    if not helmetStatus:
        helmetStatus = True
        expenses += helmetPrice
    if not swordStatus:
        swordStatus = True
        expenses += swordPrice
    if not shieldStatus:
        shieldStatus = True
        expenses += shieldPrice
    if not armorStatus:
        armorStatus = True
        expenses += armorPrice

    n += 1

print(f"Gladiator expenses: {expenses:.2f} aureus")