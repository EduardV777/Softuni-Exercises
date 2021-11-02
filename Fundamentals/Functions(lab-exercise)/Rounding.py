sequence=input()
def roundingList(seq):
    k=0; list1=[]
    while k<len(seq):
        num=""
        if seq[k]!=" ":
            for j in range(k,len(seq)):
                if seq[j]!=" ":
                    num+=seq[j]
                    k+=1
                else:
                    k+=1
                    break
            num=round(float(num))
            list1.append(num)
        else:
            k+=1
    print(list1)
roundingList(sequence)
