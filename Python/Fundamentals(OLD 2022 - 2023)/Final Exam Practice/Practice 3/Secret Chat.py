import re
msg=input()
msg=[char for char in msg]
specs=["?","*","+"]
while True:
    command=input()
    if command!="Reveal":
        match = False
        if "InsertSpace" in command:
            command=command.split(":|:")
            ind=int(command[1])
            msg.insert(ind," ")
            match=True
        elif "Reverse" in command:
            command=command.split(":|:")
            subStr=command[1]
            for k in specs:
                if k in subStr:
                    index=subStr.index(k)
                    subStr=[e for e in subStr]
                    subStr.insert(index,"\\")
                    subStr=''.join(subStr)
            findSubStr=re.compile(subStr)
            msg=''.join(msg)
            occurrences=findSubStr.finditer(msg)
            msg=[char for char in msg]
            for j in occurrences:
                match=True
                inds=j.span()
                startInd=inds[0]; endInd=inds[1]-1
                subMsg=""
                while endInd>=startInd:
                    subMsg+=msg[startInd]
                    del msg[startInd]
                    endInd-=1
                subMsg=[e for e in subMsg]
                subMsg.reverse()
                subMsg=''.join(subMsg)
                msg.append(subMsg)
                break
            if match==False:
                print("error")
        elif "ChangeAll" in command:
            match=True
            command=command.split(":|:")
            subStr=command[1]; replacement=command[2]
            pattern=rf"({subStr})"
            msg=''.join(msg)
            newMsg=re.sub(pattern,replacement,msg)
            msg=newMsg
            msg=[e for e in msg]
        if match==True:
            print(''.join(msg))
    else:
        print(f"You have a new text message: {''.join(msg)}")
        break
