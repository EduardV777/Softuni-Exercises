guests=int(input())
reservations=set([])

while guests!=0:
    reservationCode=input()
    reservations.add(reservationCode)
    guests-=1

while True:
    r=input()
    if r!="END":
        reservations.discard(r)
    else:
        print(len(reservations))
        VIPS=[]; Regulars=[]
        for e in reservations:
            if e[0].isnumeric():
                VIPS.append(e)
            else:
                Regulars.append(e)
        VIPS.sort(); Regulars.sort()
        for k in VIPS:
            print(k)
        for k in Regulars:
            print(k)
        break