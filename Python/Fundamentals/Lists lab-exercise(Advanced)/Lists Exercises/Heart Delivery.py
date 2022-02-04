integers=input()
neighbourhood=[]; everyHouseHadVD=True
k=0
while k<len(integers):
    val=""
    if integers[k]!="@":
        for j in range(k,len(integers)):
            if integers[j]!="@":
                val+=integers[j]
                k+=1
            else:
                break
        val=int(val)
        neighbourhood.append(val)
    else:
        k+=1
command=""; cupidPos=0
while command!="Love!":
    command=input()
    if command!="Love!":
        if "Jump" in command:
            length=""
            k=5
            while k<len(command):
                length+=command[k]
                k+=1
            length=int(length)
            cupidPos+=length
            if cupidPos>len(neighbourhood)-1:
                cupidPos=0
            if neighbourhood[cupidPos]==0:
                print(f"Place {cupidPos} already had Valentine's day.")
            else:
                neighbourhood[cupidPos]-=2
                if neighbourhood[cupidPos]==0:
                    print(f"Place {cupidPos} has Valentine's day.")
    else:
        housesSkippedVD=0
        for j in range(0,len(neighbourhood)):
            if neighbourhood[j]>0:
                housesSkippedVD+=1
                everyHouseHadVD=False
        print(f"Cupid's last position was {cupidPos}.")
        if everyHouseHadVD==True:
            print("Mission was successful.")
            del housesSkippedVD
        else:
            print(f"Cupid has failed {housesSkippedVD} places.")
