collectionOfTickets=input()
collectionOfTickets=collectionOfTickets.split(", ")

for k in range(0,len(collectionOfTickets)):
    collectionOfTickets[k]=collectionOfTickets[k].replace(" ", "")

for k in range(0,len(collectionOfTickets)):
    if not len(collectionOfTickets[k])==20:
        print("invalid ticket")
        continue
    else:
        jackpotCheck=["@",0,0]
        firstHalf=0; secondHalf=0; newSymbolFound=False
        symbs=0; half="first"
        for j in range(0,len(collectionOfTickets[k])):
            if j>=len(collectionOfTickets[k])/2 and half=="first":
                half="second"; symbs=0
            if len(collectionOfTickets[k])==20:
                if collectionOfTickets[k][j]=="@" or collectionOfTickets[k][j]=="#" or collectionOfTickets[k][j]=="$" or collectionOfTickets[k][j]=="^":
                    if jackpotCheck[0]!=collectionOfTickets[k][j]:
                        symbs=0
                        jackpotCheck[0]=collectionOfTickets[k][j]
                    symbs+=1
                    if half=="first":
                        if symbs>firstHalf:
                            firstHalf+=(symbs-firstHalf)
                            jackpotCheck[1]+=1
                    else:
                        if symbs>secondHalf:
                            secondHalf+=(symbs-secondHalf)
                            jackpotCheck[2]+=1
                else:
                    symbs=0
        if jackpotCheck[1]>=10 and jackpotCheck[2]>=10:
            print(f"ticket \"{collectionOfTickets[k]}\" - {jackpotCheck[1]}{jackpotCheck[0]} Jackpot!")
        else:
            if firstHalf>=6 and secondHalf>=6:
                #If there are more on any one side, we adjust the value of second half to display the correct amount of matching symbols on both sides
                if secondHalf>firstHalf:
                    secondHalf=firstHalf
                if firstHalf>secondHalf:
                    firstHalf=secondHalf
                print(f"ticket \"{collectionOfTickets[k]}\" - {secondHalf}{jackpotCheck[0]}")
            else:
                print(f"ticket \"{collectionOfTickets[k]}\" - no match")
