n=int(input())
parking=set([])
while n!=0:
    parkInfo=input(); parkInfo=parkInfo.split(", ")
    if parkInfo[0]=="IN":
        parking.add(parkInfo[1])
    elif parkInfo[0]=="OUT":
        parking.discard(parkInfo[1])
    n-=1

if len(parking)>0:
    while len(parking)!=0:
        print(parking.pop())
else:
    print("Parking Lot is Empty")