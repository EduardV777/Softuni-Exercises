str1=input(); str2=input(); str3=input()
strings=[]
strings.append(str1); strings.append(str2); strings.append(str3)
for k in range(0,2):
    for j in range(0,len(strings)):
        if strings[j].find("head")>-1 and j>0:
            temp=strings[0]
            strings[0]=strings[j]
            strings[j]=temp
        elif strings[j].find("body")>-1 and j>1:
            temp=strings[1]
            strings[1]=strings[j]
            strings[j]=temp
        elif strings[j].find("tail")>-1 and j<2:
            temp=strings[2]
            strings[2]=strings[j]
            strings[j]=temp
print(strings)
