n=int(input())
heroes={}
for k in range(0,n):
    heroData=input()
    heroData=heroData.split(" ")
    heroes[heroData[0]]=[int(heroData[1]), int(heroData[2])]
while True:
    command=input()
    if command!="End":
        if "CastSpell" in command:
            command=command.split(" - ")
            hero=command[1]; MP=int(command[2])
            spell=command[3]
            if heroes[hero][1]>=MP:
                heroes[hero][1]-=MP
                print(f"{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!")
            else:
                print(f"{hero} does not have enough MP to cast {spell}!")
        elif "TakeDamage" in command:
            command = command.split(" - ")
            hero=command[1]; dmg=int(command[2])
            attacker=command[3]
            heroes[hero][0]-=dmg
            if heroes[hero][0]>0:
                print(f"{hero} was hit for {dmg} HP by {attacker} and now has {heroes[hero][0]} HP left!")
            else:
                del heroes[hero]
                print(f"{hero} has been killed by {attacker}!")
        elif "Recharge" in command:
            command = command.split(" - ")
            hero=command[1]; amount=int(command[2])
            heroes[hero][1]+=amount
            if heroes[hero][1]>200:
                amount=200-(heroes[hero][1]-amount)
                heroes[hero][1]=200
            print(f"{hero} recharged for {amount} MP!")
        elif "Heal" in command:
            command = command.split(" - ")
            hero=command[1]; amount=int(command[2])
            heroes[hero][0]+=amount
            if heroes[hero][0]>100:
                amount = 100-(heroes[hero][0] - amount)
                heroes[hero][0]=100
            print(f"{hero} healed for {amount} HP!")
    else:
        for j in heroes:
            print(f"{j}\nHP: {heroes[j][0]}\nMP: {heroes[j][1]}")
        break
