import re
someStr=input()
someStr=[c for c in someStr]
specs=["?", "+", "*", "|"]
while True:
    command=input()
    if command!="Done":
        if "TakeOdd" in command:
            newPass=""
            for k in range(0,len(someStr)):
                if k%2!=0:
                    newPass+=someStr[k]
            someStr=newPass
            print(someStr)
            someStr=[c for c in someStr]
        elif "Cut" in command:
            command=command.split(" ")
            index=int(command[1]); length=int(command[2])
            subStr=""
            for k in range(index,index+length):
                subStr+=someStr[k]
            for j in range(0,len(specs)):
                if specs[j] in subStr:
                    subStr.insert(j,"\\")
            findSub=re.compile(rf"{subStr}")
            someStr=''.join(someStr)
            occurrences=findSub.finditer(someStr)
            someStr=[e for e in someStr]
            for j in occurrences:
                indexes=j.span()
                startInd=indexes[0]; endInd=indexes[1]-1
                while endInd>=startInd:
                    del someStr[startInd]
                    endInd-=1
                break
            print(''.join(someStr))
        elif "Substitute" in command:
            command=command.split(" ")
            subStr=command[1]; substitute=command[2]
            subStr = [e for e in subStr]
            for j in range(0,len(specs)):
                if specs[j] in subStr:
                    index=subStr.index(specs[j])
                    subStr.insert(index,"\\")
            subStr = ''.join(subStr)
            someStr=''.join(someStr)
            newStr=re.sub(subStr,substitute,someStr)
            if newStr==someStr:
                print("Nothing to replace!")
            else:
                someStr=newStr
                print(someStr)
                someStr=[c for c in someStr]
    else:
        print(f"Your password is: {''.join(someStr)}")
        break
