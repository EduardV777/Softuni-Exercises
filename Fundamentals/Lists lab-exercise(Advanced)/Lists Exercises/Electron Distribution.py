electrons=int(input())
shells=1; filledShells=[]
while True:
    if electrons<1:
        break
    nElectrons=2*shells**2
    shellSpace=nElectrons; filledElectrons=0
    while shellSpace>0:
        nElectrons-=1; electrons-=1; shellSpace-=1
        filledElectrons+=1
        if electrons==0:
            break
    filledShells.append(filledElectrons)
    shells+=1
print(filledShells)
