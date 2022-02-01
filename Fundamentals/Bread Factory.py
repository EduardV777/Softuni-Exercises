events=input()
events=events.split("|")
energy=100; coins=100; handledEverything=True
for k in range(0,len(events)):
    currEvent=events[k].split("-")
    if currEvent[0]=="rest":
        currEnergy=energy
        if energy+int(currEvent[1])<=100:
            energy+=int(currEvent[1])
        print(f"You gained {energy-currEnergy} energy.")
        print(f"Current energy: {energy}.")
    elif currEvent[0]=="order":
        if energy>=30:
            coins += int(currEvent[1])
            energy-=30
            print(f"You earned {int(currEvent[1])} coins.")
        else:
            energy+=50
            print("You had to rest!")
    else:
        if coins>=int(currEvent[1]):
            print(f"You bought {currEvent[0]}.")
            coins-=int(currEvent[1])
        else:
            print(f"Closed! Cannot afford {currEvent[0]}.")
            handledEverything=False; break
if handledEverything==True:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
