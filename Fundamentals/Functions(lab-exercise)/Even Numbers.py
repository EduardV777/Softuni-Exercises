seq=input()
def CheckEven(n):
    if n%2==0:
        return True
    else:
        return False

def ProcessSequence(sequence):
    k=0; numbers=[]
    while k<len(sequence):
        num=""
        if sequence[k]!=" ":
            for j in range(k,len(sequence)):
                if sequence[j]!=" ":
                    num+=sequence[j]
                    k+=1
                else:
                    k+=1
                    break
            num=int(num)
            numbers.append(num)
        else:
            k+=1
    evenNumbers=filter(CheckEven,numbers)
    numbers=list(evenNumbers)
    print(numbers)
ProcessSequence(seq)
