matrixSize=input()
matrixSize=matrixSize.split(", "); matrixSize=[int(i) for i in matrixSize]
rows=matrixSize[0]; columns=matrixSize[1]
k=0
matrixList=[]

while k<rows:
    matrix=input()
    matrix=matrix.split(" "); matrix=[int(e) for e in matrix]
    e=0; elements=len(matrix)
    matrixList.append([])
    while e < columns:
        matrixList[k].append(matrix[0])
        del matrix[0]
        e += 1
    k+=1

e=0; r=0
while e<columns:
   sum=0; r=0
   while r<rows:
       sum+=matrixList[r][e]
       r+=1
   print(sum)
   e+=1