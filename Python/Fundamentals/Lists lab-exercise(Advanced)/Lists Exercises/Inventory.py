items=input()
inventory=[]
k=0
while k<len(items):
    itemName=""
    if items[k]!=" ":
        for j in range(k,len(items)):
            if items[j]!=",":
                itemName+=items[j]
                k+=1
            else:
                k+=1
                break
        inventory.append(itemName)
    else:
        k+=1

command=""
while command!="Craft!":
    command=input()
    if command!="Craft!":
        if "Collect" in command:
            itemName=""
            k=7
            while k<len(command):
                if command[k]!=" " and command[k]!="-":
                    for j in range(k,len(command)):
                        itemName+=command[j]
                        k+=1
                else:
                    k+=1
            for i in range(0,len(inventory)):
                if inventory[i]==itemName:
                    contr=i
                    break
                else:
                    contr=-3
            if contr==-3:
                inventory.append(itemName)
        elif "Drop" in command:
            itemName=""
            k=4
            while k<len(command):
                if command[k]!=" " and command[k]!="-":
                    for j in range(k,len(command)):
                        itemName+=command[j]
                        k+=1
                else:
                    k+=1
            for i in range(0,len(inventory)):
                if inventory[i]==itemName:
                    del inventory[i]
                    break
        elif "Combine" in command:
            oldItem=""; newItem=""
            k=13; stoppedAt=0
            while k<len(command):
                if command[k]!=" " and command[k]!="-" and command[k]!=":":
                    for j in range(k,len(command)):
                        if command[j]!=":":
                            if stoppedAt==0:
                                oldItem+=command[j]
                            else:
                                newItem+=command[j]
                            k+=1
                        else:
                            stoppedAt = k
                            break
                else:
                    k+=1
            for i in range(0,len(inventory)):
                if inventory[i]==oldItem:
                    inventory.insert(i+1,newItem)
                    break
        elif "Renew" in command:
            itemName=""
            k=5
            while k<len(command):
                if command[k]!=" " and command[k]!="-":
                    for j in range(k,len(command)):
                        itemName+=command[j]
                        k+=1
                else:
                    k+=1
            for i in range(0,len(inventory)):
                if inventory[i]==itemName:
                    saveItemName=itemName
                    del inventory[i]
                    inventory.append(itemName)
                    break
    else:
        print(", ".join(inventory))
