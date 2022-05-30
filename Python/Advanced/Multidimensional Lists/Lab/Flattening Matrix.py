rows=input()
rows=int(rows)
k=0
matrixList=[]; flattenedMatrix=[]

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

flattenedMatrix=[num for l in matrixList for num in l]
print(flattenedMatrix)