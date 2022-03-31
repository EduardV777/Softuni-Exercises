rawKey=input()
#only letters and nums
while True:
    command=input()
    if command!="Generate":
        if "Contains" in command:
            command=command.split(">>>")
            subStr=command[1]
            findStr=rawKey.find(subStr)
            if findStr!=-1:
                print(f"{rawKey} contains {subStr}")
            else:
                print("Substring not found!")
        elif "Flip" in command:
            command = command.split(">>>")
            case=command[1]
            startInd=int(command[2]); endInd=int(command[3])
            rawKey=[e for e in rawKey]
            for k in range(startInd,endInd):
                if case=="Upper":
                    rawKey[k]=rawKey[k].upper()
                elif case=="Lower":
                    rawKey[k]=rawKey[k].lower()
            rawKey=''.join(rawKey)
            print(f"{rawKey}")
        elif "Slice" in command:
            command = command.split(">>>")
            startInd=int(command[1]); endInd=int(command[2])-1
            rawKey=[e for e in rawKey]
            while endInd>=startInd:
                del rawKey[startInd]
                endInd-=1
            rawKey=''.join(rawKey)
            print(f"{rawKey}")
    else:
        print(f"Your activation key is: {''.join(rawKey)}")
        break
