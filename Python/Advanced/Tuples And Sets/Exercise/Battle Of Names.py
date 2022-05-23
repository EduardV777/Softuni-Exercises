import math
n=int(input())
row=1

oddSet=set([]); evenSet=set([])
while n:
    name=input()
    asciiSum=0
    for k in name:
        asciiSum+=ord(k)
    asciiSum/=row
    asciiSum=math.floor(asciiSum)
    if asciiSum%2==0:
        evenSet.add(asciiSum)
    else:
        oddSet.add(asciiSum)
    n-=1; row+=1

sumSet1=0; sumSet2=0
for k in oddSet:
    sumSet1+=k
for k in evenSet:
    sumSet2+=k

output=""
if sumSet1==sumSet2:
    unionSet=oddSet.union(evenSet)
    while len(unionSet):
        output+=str(unionSet.pop())
        if len(unionSet)!=0:
            output+=", "
elif sumSet1>sumSet2:
    differenceSet=oddSet.difference(evenSet)
    while len(differenceSet):
        output+=str(differenceSet.pop())
        if len(differenceSet)!=0:
            output+=", "
elif sumSet1<sumSet2:
    symmetricDiffSet=oddSet.symmetric_difference(evenSet)
    while len(symmetricDiffSet):
        output+=str(symmetricDiffSet.pop())
        if len(symmetricDiffSet)!=0:
            output+=", "

print(output)