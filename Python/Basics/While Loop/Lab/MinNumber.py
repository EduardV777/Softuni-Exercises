minN = "EMPTY"

while True:
    com = input()

    if com != "Stop":
        if minN == "EMPTY":
            minN = int(com)
        else:
            if int(com) < minN:
                minN = int(com)
    else:
        break

print(minN)