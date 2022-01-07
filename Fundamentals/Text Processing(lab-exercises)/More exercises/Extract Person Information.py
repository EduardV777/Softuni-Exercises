n=int(input())
for k in range(0,n):
    string=input()
    name=""; age=""
    nameInd=string.find("@")
    if nameInd!=-1:
        for j in range(nameInd+1,len(string)):
            if string[j]!="|":
                name+=string[j]
            else:
                break
    ageInd=string.find("#")
    if ageInd!=-1:
        for j in range(ageInd+1,len(string)):
            if string[j]!="*":
                age+=string[j]
            else:
                break
    print(f"{name} is {age} years old.")
