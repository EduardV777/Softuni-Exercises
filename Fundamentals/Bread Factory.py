events=input()
eventsList=[]; energy=100; coins=100; closed=False
k=0
while k<len(events):
    eventName=""; eventVal=""
    if events[k]!="-" or events[k]!="|":
        if events[k].isalpha():
            for j in range(k,len(events)):
                if events[j]!="-":
                    k+=1
                    eventName+=events[j]
                else:
                    k+=1
                    break
            eventsList.append([eventName])
        elif events[k].isdigit():
            for j in range(k,len(events)):
                if events[j]!="|":
                    k+=1
                    eventVal+=events[j]
                else:
                    k+=1
                    break
            eventsList[len(eventsList)-1].append(int(eventVal))
for k in range(0,len(eventsList)):
    for j in range(0,1):
        if eventsList[k][j]=="rest":
            gainedEnergy = 100
            if not energy+eventsList[k][j+1]>100:
                initialEnergy=energy
                energy+=eventsList[k][j+1]
                gainedEnergy=energy-initialEnergy
            else:
                energy=100
                gainedEnergy-=energy
            print(f"You gained {gainedEnergy} energy.\nCurrent energy: {energy}.")
        elif eventsList[k][j]=="order":
            if not energy-30<1:
                energy-=30
                earned=eventsList[k][j+1]
                coins+=earned
                print(f"You earned {earned} coins.")
            else:
                energy+=50
                print("You had to rest!")
        else:
            if coins>=eventsList[k][j+1]:
                coins-=eventsList[k][j+1]
                print(f"You bought {eventsList[k][j]}.")
            else:
                closed=True
                print(f"Closed! Cannot afford {eventsList[k][j]}.")
                break
    if closed==True:
        break
if closed==False:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
