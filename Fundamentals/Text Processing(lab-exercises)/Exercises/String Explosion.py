string=input()
finalString=""
k=0
while k<len(string):
    if string[k]!=">":
        finalString+=string[k]
        k+=1
    else:
        resume=False
        finalString+=string[k]
        k+=1
        j=int(string[k])
        while k<len(string):
            if j==0:
                resume=True
                break
            while j!=0:
                if not k<len(string):
                    j=0
                    break
                if string[k]==">":
                    finalString+=string[k]
                    k+=1
                    j+=int(string[k])
                else:
                    k+=1; j-=1
        if resume==False:
            break
print(finalString)
