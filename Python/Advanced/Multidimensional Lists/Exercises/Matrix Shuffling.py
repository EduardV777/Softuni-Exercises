matrixSizes=input()
matrixSizes=matrixSizes.split(" "); matrixSizes=[int(e) for e in matrixSizes]
matrix=[]

def Show(matrixToShow):
    output=""
    for k in range(0,len(matrixToShow)):
        for j in range(0, len(matrixToShow[k])):
            output+=matrixToShow[k][j]+" "
        if k!=len(matrixToShow)-1:
            output+="\n"
    return output

for k in range(0,matrixSizes[0]):
    row=input()
    row=row.split(" ")
    matrix.append([num for num in row])


while True:
    error=False
    command=input()
    if command!="END":
        if "swap" in command:
            command=command.split(" ")
            if not len(command)==5:
                error=True
            else:
                del command[0]
                command=[int(e) for e in command]

            if error==False:
                for k in range(0,len(command)):
                    if command[k]<0 or command[k]>=len(command):
                        error=True
                        break

            if error==False:
                row=command[0]; col=command[1]
                row2=command[2]; col2=command[3]
                tempVal=matrix[row][col]
                matrix[row][col]=matrix[row2][col2]
                matrix[row2][col2]=tempVal
                print(Show(matrix))
        else:
            error=True

        if error==True:
            print('Invalid input!')
    else:
        break