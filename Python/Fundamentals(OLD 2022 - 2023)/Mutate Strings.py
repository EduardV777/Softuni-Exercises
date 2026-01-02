string1=input(); string2=input()
strToReplace=[]; temp=""; doNotShow=False
if string1!=string2:
    for k in range(0,len(string1)):
        strToReplace.append(string1[k])
    for k in range(0,len(string1)):
        if strToReplace[k]==" ":
            doNotShow=True
        strToReplace[k]=string2[k]
        output="".join(strToReplace)
        if temp==output:
            continue
        temp="".join(strToReplace)
        if string2[k]!=" ":
            doNotShow=False
        if output!=string1 and doNotShow==False:
            print(output)
            doNotShow=False
