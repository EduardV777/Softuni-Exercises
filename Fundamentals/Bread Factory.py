workEvents=input()
workEvents=workEvents.split("|")
energy=100; coins=100; closedBakery=False
for k in range(0,len(workEvents)):
    workEvents[k]=workEvents[k].split("-")
    workEvents[k][1]=int(workEvents[k][1])

for j in range(0,len(workEvents)):
    if workEvents[j][0]=="rest":
        if energy+workEvents[j][1]>100:
            energy=100
            print(f"You gained 0 energy.")
        else:
            print(f"You gained {workEvents[j][1]} energy.")
            energy+=workEvents[j][1]
        print(f"Current energy: {energy}.")
    elif workEvents[j][0]=="order":
        if energy>=30:
            print(f"You earned {workEvents[j][1]} coins.")
            coins += workEvents[j][1]
            energy-=30
        else:
            print("You had to rest!")
            energy+=50
    else:
        if coins>=workEvents[j][1]:
            print(f"You bought {workEvents[j][0]}.")
            coins-=workEvents[j][1]
        else:
            print(f"Closed! Cannot afford {workEvents[j][0]}.")
            closedBakery=True
            break
if closedBakery==False:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
