matrixData=input()
matrixData=matrixData.split(", ")
rows=int(matrixData[0]); cols=int(matrixData[1])

matrix=[]; subMatrix=[]
biggestSum=0

for k in range(0,rows):
    matrix.append([])
    rowEntry=input()
    rowEntry=rowEntry.split(", ")
    for j in range(0,len(rowEntry)):
        matrix[k].append(int(rowEntry[j]))

r=0

while r<=rows:
    c=0
    while c<=cols:
        currMatrix=[[],[]]; sum=0
        try:
            currMatrix[0].append(matrix[r][c])
            sum+=matrix[r][c]
            currMatrix[0].append(matrix[r][c+1])
            sum +=matrix[r][c+1]

            currMatrix[1].append(matrix[r+1][c])
            sum +=matrix[r+1][c]
            currMatrix[1].append(matrix[r+1][c+1])
            sum +=matrix[r+1][c+1]

            if sum > biggestSum:
                biggestSum = sum
                subMatrix = [l for l in currMatrix]
        except IndexError:
            pass
        c+=1
    r+=1

output=""
for k in range(0,len(subMatrix)):
    for j in range(0,len(subMatrix[k])):
        output+=str(subMatrix[k][j])+" "
    if k!=len(subMatrix)-1:
        output+="\n"
print(output)
print(biggestSum)