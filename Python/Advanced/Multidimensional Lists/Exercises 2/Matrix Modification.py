n=int(input())

matrix=[]

for k in range(0,n):
    row=input()
    row=row.split(" ")
    matrix.append([int(e) for e in row])

while True:
    command=input()
    if command!="END":
        if "Add" in command:
            command=command.split(" ")
            row=int(command[1]); col=int(command[2]); val=int(command[3])
            if row>=n or col>=n or row<0 or col<0:
                print("Invalid coordinates")
                continue
            matrix[row][col]+=val
        elif "Subtract" in command:
            command = command.split(" ")
            row = int(command[1]); col = int(command[2]); val = int(command[3])
            if row>=n or col>=n or row<0 or col<0:
                print("Invalid coordinates")
                continue
            matrix[row][col]-=val
    else:
        break

for k in range(0,len(matrix)):
    matrix[k]=[str(e) for e in matrix[k]]
    print(f"{' '.join(matrix[k])}")