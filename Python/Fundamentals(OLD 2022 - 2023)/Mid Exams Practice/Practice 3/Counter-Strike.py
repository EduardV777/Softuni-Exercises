energy=int(input())
wonBattles=0
while True:
    distance=input()
    if distance!="End of battle":
        distance=int(distance)
        if distance<=energy:
            energy-=distance
            wonBattles+=1
            if wonBattles%3==0:
                energy+=wonBattles
        else:
            print(f"Not enough energy! Game ends with {wonBattles} won battles and {energy} energy")
            break
    else:
        print(f"Won battles: {wonBattles}. Energy left: {energy}")
        break
