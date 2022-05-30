matrixSize=input()

matrixSize=matrixSize.split(", ")
rows=int(matrixSize[0]); elements=int(matrixSize[1])
sum=0; k=0
matrixList=[]

while rows!=0:
    matrix=input()
    matrix=matrix.split(", "); matrix=[int(e) for e in matrix]
    e=0
    matrixList.append([])
    while e < elements:
        sum += matrix[0]
        matrixList[k].append(matrix[0])
        del matrix[0]
        e += 1
    rows-=1; k+=1
print(sum)
print(matrixList)