forceBook={}
while True:
    command=input()
    if "|" in command:
        forceBookUser=command.split(" | ")
        sideName=forceBookUser[0]; username=forceBookUser[1]
        noUserAndSide=True
        for j in forceBook:
            if j==sideName:
                noUserAndSide=False
                userFound=False
                for k in range(0,len(forceBook[j])):
                    if username==forceBook[j][k]:
                        userFound=True
                        break
                if userFound==False:
                    forceBook[j].append(username)
        if noUserAndSide==True:
            forceBook[sideName]=[username]
    elif "->" in command:
        forceBookUser=command.split(" -> ")
        username=forceBookUser[0]; sideName=forceBookUser[1]
        noSide=True
        for j in forceBook:
            if j==sideName:
                noSide=False
        if noSide==True:
            forceBook[sideName]=[]
        noUser=True
        for j in forceBook:
            try:
                ind=forceBook[j].index(username)
                forceBook[sideName].append(username)
                noUser=False
                del forceBook[j][ind]
            except:
                continue
        if noUser==True:
            forceBook[sideName].append(username)
        print(f"{username} joins the {sideName} side!")
    elif command=="Lumpawaroo":
        for j in forceBook:
            forceBook[j].insert(0,len(forceBook[j]))
        orderDescByForce=sorted(forceBook.items(),key=lambda x: x[1][0], reverse=True)
        orderDescByForce=dict(orderDescByForce)
        for j in orderDescByForce:
            del orderDescByForce[j][0]
        orderByName=sorted(orderDescByForce.items(), key=lambda x: x[1])
        orderByName=dict(orderByName)
        for j in orderByName:
            members=len(orderByName[j])
            orderByName[j].sort()
            if members != 0:
                print(f"Side: {j}, Members: {members}")
                for k in range(0,len(orderByName[j])):
                    print(f"! {orderByName[j][k]}")
            else:
                continue
        break
