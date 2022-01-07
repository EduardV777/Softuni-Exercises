key=input()
stringList=[]; key=key.split(" ")

while True:
    command=input()
    if command!="find":
        stringList.append(command)
    else:
        break


def LoopThroughStrings(findTreasureInfo=False):

    for k in range(0,len(stringList)):
        ind=0
        newString=""
        if findTreasureInfo==False:
            for j in range(0,len(stringList[k])):
                if ind>=len(key):
                    ind=0
                char=ord(stringList[k][j]); char-=int(key[ind]); char=chr(char)
                newString+=char
                ind+=1

            stringList[k]=newString
        else:
            typeInd=stringList[k].find("&")
            type=""; coordinates=""
            if typeInd!=-1:
                for j in range(typeInd+1,len(stringList[k])):
                    if stringList[k][j]!="&":
                        type+=stringList[k][j]
                    else:
                        break
            coordinatesInd=stringList[k].find("<")
            if coordinatesInd!=-1:
                for j in range(coordinatesInd+1,len(stringList[k])):
                    if stringList[k][j]!=">":
                        coordinates+=stringList[k][j]
                    else:
                        break
            print(f"Found {type} at {coordinates}")

LoopThroughStrings()
LoopThroughStrings(True)
