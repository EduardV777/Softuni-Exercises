energy = 100
coins = 100

events = input().split("|")

dayComplete = True

for k in range(0, len(events)):
    if "rest" in events[k]:
        amountEnergy = int(events[k].split("-")[1])
        if amountEnergy + energy > 100:
            amountEnergy = 100 - energy
        else:
            energy += amountEnergy

        print(f"You gained {amountEnergy} energy.")
        print(f"Current energy: {energy}.")

    elif "order" in events[k]:
        energy -= 30

        if energy < 0:
            energy = 50
            print("You had to rest!")
            continue
        else:
            earnings = int(events[k].split("-")[1])
            coins += earnings
            print(f"You earned {earnings} coins.")

    else:
        ingredient = events[k].split("-")[0]
        price = int(events[k].split("-")[1])

        if coins >= price:
            coins -= price
            print(f"You bought {ingredient}.")

        else:
            print(f"Closed! Cannot afford {ingredient}.")
            dayComplete = False
            break

if dayComplete:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")