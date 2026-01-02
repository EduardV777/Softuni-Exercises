seq=input()
def SortList(sequence):
    k=0; list1=[]
    while k<len(sequence):
        num=""
        if sequence[k]!=" ":
            for j in range(k,len(sequence)):
                if sequence[k]!=" ":
                    num+=sequence[k]
                    k+=1
                else:
                    k+=1
                    break
            num=int(num)
            list1.append(num)
        else:
            k+=1
    print(sorted(list1))
SortList(seq)
