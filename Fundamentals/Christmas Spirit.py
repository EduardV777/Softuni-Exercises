qty=int(input()); days=int(input())
christmasSpirit=0; totalCost=0
for k in range(1,days+1):
    boughtSkirtsAndGarlands=False
    if k%11==0:
        qty+=2
    if k%2==0:
        totalCost+=2*qty; christmasSpirit+=5
    if k%3==0:
        totalCost+=(5*qty)+(3*qty); christmasSpirit+=13
        boughtSkirtsAndGarlands=True
    if k%5==0:
        totalCost+=15*qty; christmasSpirit+=17
        if boughtSkirtsAndGarlands==True:
            boughtSkirtsAndGarlands=False
            christmasSpirit+=30
    if k%10==0:
        christmasSpirit-=20
        totalCost+=5+3+15
        if k==days:
            christmasSpirit-=30
print(f"Total cost: {totalCost}\nTotal spirit: {christmasSpirit}")
