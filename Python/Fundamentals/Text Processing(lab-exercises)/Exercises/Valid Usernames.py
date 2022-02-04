usernames=input()
usernameList=usernames.split(", ")
k=0
while k<len(usernameList):
    valid=False
    if 3<=len(usernameList[k])<=16:
        for j in range(0,len(usernameList[k])):
            if usernameList[k][j].isdigit() or usernameList[k][j].isalpha() or usernameList[k][j]=="-" or usernameList[k][j]=="_":
                valid=True
            else:
                valid=False
                break
        if valid==False:
            del usernameList[k]
            continue
        else:
            k+=1
    else:
        del usernameList[k]
print("\n".join(usernameList))
