matrixSizes=input()
matrixSizes=matrixSizes.split(" "); matrixSizes=[int(e) for e in matrixSizes]

matrix=[]
sqMatrices2x2Found=0

for row in range(0, matrixSizes[0]):
    row=input()
    row=row.split(" ")
    matrix.append([e for e in row])

for k in range(0, len(matrix),+1):
    c=0
    while c<matrixSizes[1]:
        if not c+1>=len(matrix[k]) and not k+1>=len(matrix):
            if matrix[k][c]==matrix[k][c+1] and matrix[k][c]==matrix[k+1][c] and matrix[k][c]==matrix[k+1][c+1]:
                sqMatrices2x2Found+=1
        else:
            break
        c+=1

print(sqMatrices2x2Found)