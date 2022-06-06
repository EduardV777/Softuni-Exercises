n=int(input())
matrixString=""

primaryDiagonal=[]; secondaryDiagonal=[]


for k in range(0,n):
    matrixRow=input()
    matrixString+=matrixRow
    if k!=n-1:
        matrixString+="\n"

matrixString=matrixString.split("\n")

for row in range(0,n):
    matrixString[row]=matrixString[row].split(" ")


c=n-1
for k in range(0,n):
    primaryDiagonal.append(matrixString[k][k])
for j in range(0,n):
    secondaryDiagonal.append(matrixString[j][c])
    c-=1

sum1=eval('+'.join([e for e in primaryDiagonal]))
sum2=eval('+'.join([e for e in secondaryDiagonal]))
diff=abs(sum1-sum2)
print(diff)