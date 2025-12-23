#every even floor has offices
#every odd floor has apartments
#every apartment is assigned like this A{floor}{apartmentN}
#apartment and office numbers start with 0
#every office is assigned like this O{floor}{officeN}
#at the highest floor there are always apartments and they are larger than the rest
#they start with L instead of A

floors = int(input())
rooms = int(input())
r = 0
f = floors

apartment = "L"
printFormat = ""

while f != 0:
    while r < rooms:
        if f != floors:
            if f % 2 == 0:
                printFormat += f"O{f}{r} "
            else:
                printFormat += f"A{f}{r} "
        else:
            printFormat += f"L{f}{r} "

        r += 1

    r = 0
    f -= 1
    printFormat += "\n"

print(printFormat)