seq=input()
strings=seq.split(" "); finalString=""
for k in range(0,len(strings)):
    n=len(strings[k])
    finalString+=strings[k]*n
print(finalString)
