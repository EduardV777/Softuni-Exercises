string=input()
finalMsg=""; uniqueSymbs=[]
string=string.lower()
for k in range(0,len(string)):
    if string[k] in uniqueSymbs or string[k].isdigit():
        continue
    else:
        uniqueSymbs.append(string[k])
for k in range(0,len(string)):
    n=""; msgFragment=""
    if string[k].isdigit():
        n+=string[k]
        ind=k
        for j in range(k+1,len(string)):
            if string[j].isdigit()==False:
                break
            else:
                n+=string[j]
        n=int(n)
        for i in range(k-1,-1,-1):
            if string[i].isdigit():
                break
            msgFragment+=string[i]
        msgFragment=reversed(msgFragment)
        msgPart=""
        for ch in msgFragment:
            msgPart+=ch
        msgPart=msgPart.upper()
        msgPart=msgPart*n
        finalMsg+=msgPart

print(f"Unique symbols used: {len(uniqueSymbs)}")
print(finalMsg)
