vacationMoney = float(input())
availableMoney = float(input())
consDays = 0
days = 0

while True:
    #spend/save
    action = input()
    amount = float(input())

    if action == "spend":
        if amount > availableMoney:
            availableMoney = 0
        else:
            availableMoney -= amount
        consDays += 1

    elif action == "save":
        availableMoney += amount
        consDays = 0


    days += 1

    if consDays == 5:
        print(f"You can't save the money.\n{days}")
        break

    if availableMoney >= vacationMoney:
        print(f"You saved the money for {days} days.")
        break