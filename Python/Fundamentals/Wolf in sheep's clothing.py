year=int(input())
happyYear=False; number=0; i=-1
while happyYear==False:
    year+=1
    year=str(year)
    if len(year)>1:
        i=0
    for k in range(i,len(year)-1):
        if len(year)==1:
            happyYear=True
            number=int(year)+1
            break
        elif len(year)==2:
            n1=int(year[k]); n2=int(year[k+1])
            if n1!=n2:
                happyYear=True
            else:
                break
        elif len(year)==3:
            n1 = int(year[k]); n2 = int(year[k + 1])
            if n1!=n2:
                happyYear=True
            else:
                happyYear=False
                break
            if int(year[0])==int(year[2]):
                happyYear=False
                break
        elif len(year)==4:
            n1 = int(year[k]); n2 = int(year[k + 1])
            if n1!=n2:
                happyYear=True
            else:
                happyYear=False
                break
            for j in range(0,2):
                if int(year[j])==int(year[j+2]):
                    happyYear=False
                    break
            if year[0]==year[3]:
                happyYear=False
                break
        elif len(year)==5:
            n1 = int(year[k]); n2 = int(year[k + 1])
            if n1!=n2:
                happyYear=True
            else:
                happyYear=False
                break
            for j in range(0,3):
                if int(year[j])==int(year[j+2]):
                    happyYear=False
                    break
            if year[0]==year[4] or year[0]==year[3] or year[1]==year[4]:
                happyYear=False
                break
    if happyYear==True:
        number=int(year)
    else:
        year=int(year)
if happyYear==True:
    print(f"{number}")
