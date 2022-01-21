giftsToBuy=input()
giftsToBuy=giftsToBuy.split(" ")
while True:
    command=input()
    if command!="No Money":
        if "OutOfStock" in command:
            command=command.split(" ")
            while True:
                if command[1] in giftsToBuy:
                    giftsToBuy[giftsToBuy.index(command[1])]="None"
                else:
                    break
        elif "Required" in command:
            command=command.split(" ")
            if not int(command[2])>=len(giftsToBuy) and not int(command[2])<0:
                giftsToBuy[int(command[2])]=command[1]
        elif "JustInCase" in command:
            command=command.split(" ")
            giftsToBuy[len(giftsToBuy)-1]=command[1]
    else:
        k=0
        while k<len(giftsToBuy):
            if giftsToBuy[k]=="None":
                del giftsToBuy[k]
            else:
                k+=1
        break
print(" ".join(giftsToBuy))
