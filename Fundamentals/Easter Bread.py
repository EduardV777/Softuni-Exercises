budget=float(input()); flourPriceKG=float(input())
eggsPackPrice=flourPriceKG*0.75; milkPriceL=flourPriceKG+(flourPriceKG*0.25)
loavesOfBread=0; milkConsumed=0; flourConsumed=0; eggsConsumed=0; collectedEggs=0
inc1=250; inc2=1; inc3=1
while budget>0:
    budgetSpent = 0; loavesOfBread+=1; collectedEggs+=3
    milkConsumed+=250; flourConsumed+=1; eggsConsumed+=1
    if milkConsumed==inc1:
        inc1+=250
        budgetSpent+=(250/1000)*milkPriceL
    if flourConsumed==inc2:
        inc2+=1
        budgetSpent+=flourPriceKG
    if eggsConsumed==inc3:
        inc3+=1
        budgetSpent+=eggsPackPrice
    if not budgetSpent>budget:
        if loavesOfBread%3==0:
            collectedEggs-=(loavesOfBread-2)
        budget-=budgetSpent
    else:
        loavesOfBread-=1
        collectedEggs-=3
        break
print(f"You made {loavesOfBread} loaves of Easter bread! Now you have {collectedEggs} eggs and {budget:.2f}BGN left.")
