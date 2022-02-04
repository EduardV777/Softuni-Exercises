currencies={'Shards': 0, 'Fragments': 0, 'Motes': 0}
obtainedItem=False
while True:
    i=0; material=""; quantity=0
    matsQty=input()
    k = 0
    while k<len(matsQty):
        matFound = False
        if matsQty[k]!=" ":
            val = ""
            for j in range(k,len(matsQty)):
                if matsQty[j]!=" ":
                    val+=matsQty[j]
                    k+=1
                else:
                    break
            if i==0:
                quantity = int(val)
                i+=1
            else:
                material = val
                for j in currencies:
                    if j.lower() == material.lower():
                        currencies[j] += quantity
                        matFound = True
                        break
                if matFound == False:
                    currencies[material] = quantity
                i-=1
        else:
            k+=1

    if currencies["Shards"]>=250:
        print("Shadowmourne obtained!")
        currencies["Shards"]-=250
        obtainedItem=True
    elif currencies["Fragments"]>=250:
        print("Valanyr obtained!")
        currencies["Fragments"]-=250
        obtainedItem = True
    elif currencies["Motes"]>=250:
        print("Dragonwrath obtained!")
        currencies["Motes"]-=250
        obtainedItem = True

    if obtainedItem==True:
        sameItemsQty=False
        for j in currencies:
            if j=="Shards":
                if currencies[j]==currencies["Fragments"]:
                    sameItemsQty=True
                    break
                elif currencies[j]==currencies["Motes"]:
                    sameItemsQty=True
                    break
            elif j=="Fragments":
                if currencies[j]==currencies["Motes"]:
                    sameItemsQty=True
                    break
        if sameItemsQty==False:
            sortCurr=sorted(currencies.items(),key=lambda k: k[1], reverse=True)
        else:
            sortCurr=sorted(currencies.items(),key=lambda k: k[0])
        sortedCurr=dict(sortCurr)
        for j in sortedCurr:
            if j=="Shards" or j=="Fragments" or j=="Motes":
                print(f"{j.lower()}: {sortedCurr[j]}")
        sortCurrJunk=sorted(currencies.items(),key=lambda k: k[0])
        sortedCurrJunk=dict(sortCurrJunk)
        for j in sortedCurrJunk:
            if j!="Shards" and j!="Fragments" and j!="Motes":
                print(f"{j}: {sortedCurrJunk[j]}")
        break
