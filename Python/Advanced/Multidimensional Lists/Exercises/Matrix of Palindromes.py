matrixSizes=input()
matrixSizes=matrixSizes.split(" "); matrixSizes=[int(e) for e in matrixSizes]

matrix=[]; char=97

def Show(matrixToShow):
    output=""
    for k in range(0,len(matrixToShow)):
        for j in range(0,len(matrixToShow[k])):
            output+=matrixToShow[k][j]+" "
        if k!=len(matrixToShow)-1:
            output+="\n"
    return output


for k in range(0, matrixSizes[0]):
    matrix.append([])
    midChar=char
    for j in range(0,matrixSizes[1]):
        palindrome=chr(char)+chr(midChar)+chr(char)
        midChar+=1
        matrix[k].append(palindrome)
    char+=1


print(Show(matrix))