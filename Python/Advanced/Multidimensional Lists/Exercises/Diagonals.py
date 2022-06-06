n=int(input())
matrixString=""
primaryDiagonal=list(); secondaryDiagonal=list()

def ShowList(matrixShow):
    output=""
    for k in range(0,len(matrixShow)):
        for j in range(0,len(matrixShow[k])):
            output+=matrixShow[k][j]+" "
        output+="\n"
    return output


for k in range(0,n):
    matrixRow=input()
    matrixString+=matrixRow
    if k!=n-1:
        matrixString+="\n"


matrixString=matrixString.split("\n")

for k in range(0,len(matrixString)):
    matrixString[k]=matrixString[k].split(", ")

matrixList=[list(e) for e in matrixString]

c=n-1
for k in range(0,len(matrixList)):
    primaryDiagonal.append(matrixList[k][k])
for j in range(0,len(matrixList)):
    secondaryDiagonal.append(matrixList[j][c])
    c-=1

print(f"Primary diagonal: {', '.join(primaryDiagonal)}. Sum: {eval('+'.join([e for e in primaryDiagonal]))}")
print(f"Secondary diagonal: {', '.join(secondaryDiagonal)}. Sum: {eval('+'.join([e for e in secondaryDiagonal]))}")



"""

3
1, 2, 3
4, 5, 6
7, 8, 9

"""