integers=input()
integers=integers.split(" "); integers=[int(e) for e in integers]
sum=0; output=""
for k in range(0,len(integers)):
    sum+=integers[k]

avgValue=sum/len(integers)
topNumbers=[e for e in integers if e>avgValue]
topNumbers.sort(reverse=True)

k=0
while k<len(topNumbers):
    if k>=5:
        break
    output+=f"{topNumbers[k]} "
    k+=1

if len(topNumbers)==0:
    print("No")
else:
    print(output)
