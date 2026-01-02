import re
stops=input()
stops=[symb for symb in stops]

def updateList(stopsList):
    stopsList=''.join(stopsList)
    stopsList = [symb for symb in stopsList]
    return stopsList

while True:
    command=input()
    if command!="Travel":
        if "Add" in command:
            command=command.split(":")
            ind=int(command[1]); string=command[2]
            if ind>=0 and ind<len(stops):
                stops.insert(ind,string)
                stops=updateList(stops)
        elif "Remove" in command:
            command=command.split(":")
            startInd=int(command[1]); endInd=int(command[2])
            if (startInd>=0 and startInd<len(stops)) and (endInd>=0 and endInd<len(stops)):
                k=startInd
                while startInd<=endInd:
                    del stops[k]
                    startInd+=1

        elif "Switch" in command:
            command=command.split(":")
            oldString=command[1]; newString=command[2]
            findStr=re.compile(rf"{oldString}")
            occurrences=findStr.finditer(''.join(stops))
            empty=True
            for j in occurrences:
                empty=False
                inds=j.span()
                startInd=inds[0]; endInd=inds[1]
                k=startInd
                while startInd<endInd:
                    del stops[k]
                    startInd+=1
            if empty==False:
                stops.insert(k,newString)
        print(''.join(stops))
    else:
        print(f"Ready for world tour! Planned stops: {''.join(stops)}")
        break
