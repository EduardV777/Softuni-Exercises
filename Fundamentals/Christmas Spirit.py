qty=int(input()); days=int(input())
cost=0; christmasSpirit=0
SecondDay=2; ThirdDay=3; FifthDay=5; TenthDay=10; EleventhDay=11
for k in range(1,days+1):
    if k==SecondDay:
        cost+=2*qty
        christmasSpirit+=5
        SecondDay+=2
    if k==ThirdDay:
        cost+=(5*qty)+(3*qty)
        christmasSpirit+=13
        ThirdDay+=3
    if k==FifthDay:
        cost+=15*qty
        christmasSpirit += 17
        if (k==TenthDay and not k==days) or (k==ThirdDay):
            christmasSpirit+=30
        FifthDay+=5
    if k==TenthDay:
        cost+=5+3+15
        christmasSpirit-=20
        if days%10==0 and k==days:
            christmasSpirit-=30
        else:
            TenthDay+=10
    if k==EleventhDay:
        qty+=2
        EleventhDay+=11
print(f"Total cost: {cost}\nTotal spirit: {christmasSpirit}")
