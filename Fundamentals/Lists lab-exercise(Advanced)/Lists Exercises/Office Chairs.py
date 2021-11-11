rooms=int(input())
freeChairs=0; LeftChairs=True
for k in range(0,rooms):
    chairs=input()
    j=0; chairsInRoom=0; visitors=""
    while j<len(chairs):
        if chairs[j]!=" ":
            for i in range(j,len(chairs)):
                if chairs[i]!=" ":
                    if chairs[i]=="X":
                        chairsInRoom+=1
                        j+=1
                    else:
                        visitors+=chairs[i]
                        j+=1
                else:
                    break
        else:
            j+=1
    visitors = int(visitors)
    if chairsInRoom<visitors:
        print(f"{visitors-chairsInRoom} more chairs needed in room {k+1}")
        LeftChairs=False
    else:
        chairsLeft=chairsInRoom-visitors
        freeChairs+=chairsLeft
if LeftChairs==True:
    print(f"Game On, {freeChairs} free chairs left")
