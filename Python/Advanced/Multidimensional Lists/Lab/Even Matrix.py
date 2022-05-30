rows=input()
rows=int(rows)
k=0
matrixList=[]; evenMatrix=[]

while rows!=0:
    matrix=input()
    matrix=matrix.split(", "); matrix=[int(e) for e in matrix]
    e=0; elements=len(matrix)
    matrixList.append([])
    while e < elements:
        matrixList[k].append(matrix[0])
        del matrix[0]
        e += 1
    rows-=1; k+=1

for k in matrixList:
    evenMatrix.append([])
    for j in k:
        if j%2==0:
            evenMatrix[len(evenMatrix)-1].append(j)
print(evenMatrix)