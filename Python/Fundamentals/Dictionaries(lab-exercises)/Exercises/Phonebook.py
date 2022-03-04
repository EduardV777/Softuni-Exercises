phonebook={}
while True:
    contact=input()
    if "-" in contact:
        contact = contact.split("-")
        phonebook[contact[0]]=contact[1]
    else:
        contact=int(contact)
        break
while contact!=0:
    searchFor=input()
    doesContactExist=phonebook.get(searchFor,"no")
    if doesContactExist=="no":
        print(f"Contact {searchFor} does not exist.")
    else:
        print(f"{searchFor} -> {phonebook[searchFor]}")
    contact-=1
