rowsColumns=input()
rowsColumns=int(rowsColumns)
k=0; n=rowsColumns; sumDiagonal=0
matrixList=[]

while n!=0:
    matrix=input()
    matrix=matrix.split(" "); matrix=[int(e) for e in matrix]
    e=0; elements=len(matrix)
    matrixList.append([])
    while e < rowsColumns:
        matrixList[k].append(matrix[0])
        del matrix[0]
        e += 1
    n-=1; k+=1

colDiagonal=0
for k in range(0,len(matrixList)):
    sumDiagonal+=matrixList[k][colDiagonal]
    colDiagonal+=1

print(sumDiagonal)