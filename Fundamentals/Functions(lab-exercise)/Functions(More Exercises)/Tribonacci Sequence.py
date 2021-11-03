numbers=int(input())
def TribonacciSeq():
    sequence=[1,1]; sequenceText=""
    for k in range(len(sequence),numbers):
        nextNum=sequence[k-1]+sequence[k-2]
        if len(sequence)>2:
            nextNum+=sequence[k-3]
        sequence.append(nextNum)
    for k in range(0,len(sequence)):
        if k>=numbers:
            break
        sequence[k] = str(sequence[k])
        sequenceText+=sequence[k]+" "
    return sequenceText
print(TribonacciSeq())
