gifts = input().split(" ")

while True:
    command = input() # OutOfStock Required JustInCase NoMoney

    if not command == "No Money":
        if "OutOfStock" in command:
            command = command.split(" ")[1]

            while True:
                if gifts.count(command) > 0:
                    ind = gifts.index(command)
                    gifts[ind] = "None"
                else:
                    break

        elif "Required" in command:
            command = command.split(" ")
            giftName = command[1]
            ind = int(command[2])

            if 0 <= ind < len(gifts):
                gifts[ind] = giftName

        elif "JustInCase" in command:
            giftName = command.split(" ")[1]

            gifts[len(gifts) - 1] = giftName



    else:
        break


while True:
    if gifts.count("None") > 0:
        gifts.remove("None")
    else:
        break

print(" ".join(gifts))