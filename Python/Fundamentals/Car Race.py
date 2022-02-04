seq=input()
times=[]
leftRacer=0; rightRacer=0
k=0
while k<len(seq):
    val=""
    if seq[k]!=" ":
        for j in range(k,len(seq)):
            if seq[j]!=" ":
                val+=seq[j]
                k+=1
            else:
                k+=1
                break
        val=int(val)
        times.append(val)
    else:
        k+=1
finishLine=len(times)//2
for k in range(0,finishLine):
    if times[k]!=0:
        leftRacer+=times[k]
    else:
        leftRacer-=leftRacer*0.2
for k in range(len(times)-1,finishLine,-1):
    if times[k]!=0:
        rightRacer+=times[k]
    else:
        rightRacer-=rightRacer*0.2
if leftRacer<rightRacer:
    print(f"The winner is left with total time: {leftRacer:.1f}")
else:
    print(f"The winner is right with total time: {rightRacer:.1f}")
