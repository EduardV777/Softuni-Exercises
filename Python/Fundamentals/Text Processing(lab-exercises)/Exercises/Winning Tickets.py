tickets=input()
tickets=tickets.split(", ")
winningSymbols=["@","#","$","^"]

for k in tickets:
    k=k.replace(" ","")
    #valid or not
    if len(k)==20:
        cursor=0
        winning=False; jackpot=False
        while True:
            ind=k.find(winningSymbols[cursor])
            if ind==-1:
                cursor+=1
                if cursor>=len(winningSymbols):
                    break
            else:
                if ind>4:
                    break
                else:
                    leftSide=0; rightSide=0
                    #check left half
                    for i in range(ind,10):
                        if k[i]==winningSymbols[cursor]:
                            leftSide+=1
                            ind+=1
                        else:
                            ind=10
                            break
                    #check right half
                    ind=k.find(winningSymbols[cursor],ind)
                    if ind==-1 or ind>14:
                        break
                    else:
                        for i in range(ind,len(k)):
                            if k[i]==winningSymbols[cursor]:
                                rightSide+=1
                            else:
                                break
                        if leftSide==10 and rightSide==10:
                            jackpot=True; winning=True
                        if leftSide==rightSide:
                            winning=True
                            break
                        else:
                            break
        if winning==False:
            print(f"ticket \"{k}\" - no match")
        else:
            output=f"ticket \"{k}\" - {leftSide}{winningSymbols[cursor]}"
            if jackpot==True:
                output+=" Jackpot!"
            print(output)
    else:
        print(f"invalid ticket")
