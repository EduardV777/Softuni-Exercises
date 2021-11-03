seq=input()
def IsItPalindrome(seq):
    k=0; list1=[]
    while k<len(seq):
        num=" "
        if seq[k]!=",":
            for j in range(k,len(seq)):
                if seq[j]!=",":
                    num+=seq[j]
                    k+=1
                else:
                    k+=2
                    break
            list1.append(num)
        else:
            k+=2
    for k in range(0,len(list1)):
        reverseVal=""
        for j in range(len(list1[k])-1,-1,-1):
            val=int(list1[k])
            reverseVal+=list1[k][j]
        if int(reverseVal)==val:
            print("True")
        else:
            print("False")
IsItPalindrome(seq)
