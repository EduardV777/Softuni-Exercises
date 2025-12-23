spaceW = int(input())
spaceL = int(input())
spaceH = int(input())

totalSpace = spaceW * spaceL * spaceH

while totalSpace >= 0:
    boxes = input()

    if boxes != "Done":
        boxes = int(boxes)
        totalSpace -= boxes
    else:
        break

if totalSpace < 0:
    print(f"No more free space! You need {abs(totalSpace)} Cubic meters more.")

else:
    print(f"{totalSpace} Cubic meters left.")