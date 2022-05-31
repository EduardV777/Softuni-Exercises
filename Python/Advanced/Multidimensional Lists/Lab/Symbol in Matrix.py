n=int(input())

squareMatrix=[]
k=0; i=0

while k<n:
    row=input()
    squareMatrix.append([])
    for j in range(0,len(row)):
        squareMatrix[i].append(row[j])
    k+=1; i+=1

symbolToFind=input()
rowFound=0; colFound=0; symbolFound=False

for k in range(0,len(squareMatrix)):
    if symbolFound==True:
        break
    for j in range(0,len(squareMatrix[k])):
        if squareMatrix[k][j]==symbolToFind:
            symbolFound=True
            rowFound=k; colFound=j

if symbolFound==True:
    print(f"({rowFound}, {colFound})")
else:
    print(f"{symbolToFind} does not occur in the matrix")