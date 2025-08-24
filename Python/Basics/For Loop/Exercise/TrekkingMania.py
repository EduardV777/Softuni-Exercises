groups = int(input())
totalPeople = 0

# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест

pcts = [0,0,0,0,0] #Musala Monblan Kilimanjaro K2 Everest

for k in range(0, groups):
    size = int(input())
    totalPeople += size

    if size <= 5:
        pcts[0] += size
    elif 6 <= size <= 12:
        pcts[1] += size
    elif 13 <= size <= 25:
        pcts[2] += size
    elif 26 <= size <= 40:
        pcts[3] += size
    elif size >= 41:
        pcts[4] += size

    if k == groups - 1:
        for i in range(0, len(pcts)):
            pcts[i] = (pcts[i] / totalPeople) * 100

            print(f"{pcts[i]:.2f}%")