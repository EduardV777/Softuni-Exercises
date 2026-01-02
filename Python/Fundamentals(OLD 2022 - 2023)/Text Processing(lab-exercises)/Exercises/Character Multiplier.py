twoStrings=input()
stringList=twoStrings.split(" ")
str1=stringList[0]; str2=stringList[1]
sum=0
k=0;j=0
while True:
    if k<len(str1):
        if j<len(str2):
            multipliedCodes=ord(str1[k])*ord(str2[j])
            sum+=multipliedCodes
            k+=1; j+=1
        else:
            sum+=ord(str1[k])
            k+=1
    else:
        if j<len(str2):
            sum+=ord(str2[j])
            j+=1
        else:
            break
print(sum)
