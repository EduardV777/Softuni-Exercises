from math import floor
groupSize=int(input()); days=int(input())
coins=0
for k in range(1,days+1):
    motivationalParty=False
    coins+=50
    if k%15==0:
        groupSize+=5
    if k%10==0:
        groupSize-=2
    coins-=2*groupSize
    if k%3==0:
        motivationalParty=True
        coins-=3*groupSize
    if k%5==0:
        coins+=20*groupSize
        if motivationalParty==True:
            coins-=2*groupSize
print(f"{groupSize} companions received {floor(coins//groupSize)} coins each.")
