import re

encryptedMsg=input()
encryptedMsg=[e for e in encryptedMsg]

while True:
    command=input()
    if command!="Decode":
        if "Move" in command:
            command=command.split("|")
            number=int(command[1])
            letters=[]
            while number!=0:
                letters.append(encryptedMsg[0])
                del encryptedMsg[0]
                number-=1
            for k in range(0,len(letters)):
                encryptedMsg.append(letters[k])
        elif "Insert" in command:
            command=command.split("|")
            ind=int(command[1]); value=command[2]
            encryptedMsg.insert(ind,value)
        elif "ChangeAll" in command:
            command=command.split("|")
            subString=command[1]; replaceWith=command[2]
            findSubString=re.compile(rf"({subString})")
            occurrences=findSubString.finditer(''.join(encryptedMsg))
            for n in occurrences:
                inds=n.span()
                start=inds[0]; end=inds[1]
                if start!=-1 and end!=-1:
                    for k in range(start,end):
                        encryptedMsg[k]=replaceWith
    else:
        print(f"The decrypted message is: {''.join(encryptedMsg)}")
        break
