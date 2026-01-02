seq=input()
def ProcessNumbers(sequence):
    k=0; list1=[]; sum=0
    while k<len(sequence):
        num=""
        if k!=" ":
            for j in range(k,len(sequence)):
                if sequence[j]!=" ":
                    num+=sequence[j]
                    k+=1
                else:
                    k+=1
                    break
            num=int(num)
            list1.append(num)
        else:
            k+=1
    #print(list1)
    for j in range(0,len(list1)):
        sum+=list1[j]
    print(f"The minimum number is {min(list1)}\nThe maximum number is {max(list1)}\nThe sum number is: {sum}")
ProcessNumbers(seq)
