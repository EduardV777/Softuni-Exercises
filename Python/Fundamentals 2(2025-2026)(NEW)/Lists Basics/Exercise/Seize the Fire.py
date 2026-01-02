cellsFire = input().split("#")
waterAmount = int(input())

effort = 0
totalFire = 0

rangesOfFireTypes = [[1, 50], [51, 80], [81, 125]]

#formatting the list with fire cells
for k in range(0, len(cellsFire)):
    fireType = cellsFire[k].split(" = ")[0]
    fireValue = int(cellsFire[k].split(" = ")[1])

    cellsFire[k] = [fireType, fireValue]

        #check validity with the given ranges
    if cellsFire[k][0] == "High":
        if not rangesOfFireTypes[2][0] <= cellsFire[k][1] <= rangesOfFireTypes[2][1]:
            cellsFire[k][0] = "Invalid"
            cellsFire[k][1] = 0

    elif cellsFire[k][0] == "Medium":
        if not rangesOfFireTypes[1][0] <= cellsFire[k][1] <= rangesOfFireTypes[1][1]:
            cellsFire[k][0] = "Invalid"
            cellsFire[k][1] = 0

    elif cellsFire[k][0] == "Low":
        if not rangesOfFireTypes[0][0] <= cellsFire[k][1] <= rangesOfFireTypes[0][1]:
            cellsFire[k][0] = "Invalid"
            cellsFire[k][1] = 0


#putting out fire cells

for k in range(0, len(cellsFire)):
    if cellsFire[k][0] != "Invalid":
        if waterAmount >= cellsFire[k][1]:
            waterAmount -= cellsFire[k][1]
            effort += cellsFire[k][1] * 0.25
            totalFire += cellsFire[k][1]
            cellsFire[k][0] = "Put out"
        else:
            continue


#preparing output
while True:
    detect = False

    for k in range(0, len(cellsFire)):
        if cellsFire[k][0] == "Invalid" or cellsFire[k][0] != "Put out":
            detect = True
            del cellsFire[k]
            break

    if not detect:
        break

print("Cells:")

for k in range(0, len(cellsFire)):
    print(f" - {cellsFire[k][1]}")

print(f"Effort: {effort:.2f}\nTotal Fire: {totalFire}")