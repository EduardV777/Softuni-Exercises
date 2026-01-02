#eggs 1 pack
#flour 1kg
#milk 250ml

budget = float(input())
flourPrice = float(input()) # pack of eggs is 75% of flour
eggPrice = flourPrice * 0.75
milkPrice = flourPrice + (flourPrice * 0.25)

coloredEggs = 0
loavesMade = 0


while True:
    expense = ((250/1000) * milkPrice) + flourPrice + eggPrice

    if budget >= expense:

        budget -= expense
        loavesMade += 1
        coloredEggs += 3

    else:
        break

    if loavesMade % 3 == 0:
        coloredEggs -= (loavesMade - 2)

print(f"You made {loavesMade} loaves of Easter bread! Now you have {coloredEggs} eggs and {budget:.2f}BGN left.")