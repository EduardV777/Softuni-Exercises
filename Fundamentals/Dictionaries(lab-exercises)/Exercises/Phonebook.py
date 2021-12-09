phoneBook={}
while True:
    contact=input()
    if "-" in contact:
        contactName=contact.split("-"); phoneNumber=contact.split("-")
        del contactName[1]; del phoneNumber[0]
        contactFound=False
        for k in phoneBook:
            if k==contactName[0]:
                phoneBook[k]=phoneNumber[0]
                contactFound=True
        if contactFound==False:
            phoneBook[contactName[0]]=phoneNumber[0]
    else:
        j=0
        while j<int(contact):
            name=input(); contactFound=False
            for i in phoneBook:
                if i==name:
                    print(f"{i} -> {phoneBook[i]}")
                    contactFound=True
            if contactFound==False:
                print(f"Contact {name} does not exist.")
            j+=1
        break
