import re
encryptedMsg=input()
encryptedMsg=[e for e in encryptedMsg]
while True:
    command=input()
    if command!="Decode":
        if "Move" in command:
            command=command.split("|")
            count=int(command[1])
            letters=[]
            while count!=0:
                letters.append(encryptedMsg[0])
                del encryptedMsg[0]
                count-=1
            for k in range(0,len(letters)):
                encryptedMsg.append(letters[k])
        elif "Insert" in command:
            command=command.split("|")
            ind=int(command[1]); val=command[2]
            encryptedMsg.insert(ind,val)
        elif "ChangeAll" in command:
            command=command.split("|")
            subStr=command[1]; replacement=command[2]
            encryptedMsg=''.join(encryptedMsg)
            encryptedMsg=encryptedMsg.replace(subStr,replacement)
            encryptedMsg=[e for e in encryptedMsg]
    else:
        print(f"The decrypted message is: {''.join(encryptedMsg)}")
        break
