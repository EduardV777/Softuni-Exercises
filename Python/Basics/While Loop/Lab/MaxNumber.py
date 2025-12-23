maxN = "EMPTY"

while True:
    com = input()

    if com != "Stop":
        if maxN == "EMPTY":
            maxN = int(com)
        else:
            if int(com) > maxN:
                maxN = int(com)
    else:
        break

print(maxN)