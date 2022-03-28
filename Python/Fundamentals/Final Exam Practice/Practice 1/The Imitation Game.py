import re
encryptedMsg=input()
encryptedMsg=[char for char in encryptedMsg]
while True:
    command=input()
    if command!="Decode":
        if "Move" in command:
            command=command.split("|")
            command[1]=int(command[1])
            letters=[]
            if command[1]<len(encryptedMsg):
                while command[1]!=0:
                    letters.append(encryptedMsg[0])
                    del encryptedMsg[0]
                    command[1]-=1
            for k in range(0,len(letters)):
                encryptedMsg.append(letters[k])
        elif "Insert" in command:
            command=command.split("|")
            ind=int(command[1]); val=command[2]
            encryptedMsg.insert(ind,val)
        elif "ChangeAll" in command:
            command=command.split("|")
            subStr=command[1]; replacement=command[2]
            findSubStr=re.compile(rf"{subStr}")
            encryptedMsg=''.join(encryptedMsg)
            foundStrings=findSubStr.finditer(encryptedMsg)
            encryptedMsg=[char for char in encryptedMsg]
            for j in foundStrings:
                indexes=j.span()
                startInd=indexes[0]; endInd=indexes[1]
                while startInd<endInd:
                    encryptedMsg[startInd]=replacement
                    startInd+=1
    else:
        print(f"The decrypted message is: {''.join(encryptedMsg)}")
        break
