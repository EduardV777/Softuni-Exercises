matrixSizes=input()
matrixSizes=matrixSizes.split(" "); matrixSizes=[int(e) for e in matrixSizes]

matrix=[]

for k in range(0,matrixSizes[0]):
    row=input()
    row=row.split(" ")
    matrix.append([int(e) for e in row])

#print(matrix)
sum=-2147000000


for row in range(0,len(matrix),+1):
    c=0
    while c<matrixSizes[1]:
        if not c+2>=len(matrix[row]) and not row+2>=len(matrix):
            currSum=(matrix[row][c]+matrix[row][c+1]+matrix[row][c+2]) + (matrix[row+1][c]+matrix[row+1][c+1]+matrix[row+1][c+2]) + (matrix[row+2][c]+matrix[row+2][c+1]+matrix[row+2][c+2])
        else:
            break

        if currSum>sum:
            sum=currSum
            subMatrix=[[ matrix[row][c], matrix[row][c+1], matrix[row][c+2] ], [ matrix[row+1][c], matrix[row+1][c+1], matrix[row+1][c+2] ], [ matrix[row+2][c], matrix[row+2][c+1], matrix[row+2][c+2] ]]
        c+=1

print(f"Sum = {sum}")
for i in range(0,len(subMatrix)):
    print(f"{' '.join([str(e) for e in subMatrix[i]])}")