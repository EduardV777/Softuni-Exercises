r=int(input())
i=1; gotOut=False; noMoves=False; rowLen=0
maze=[]
for j in range(0,r):
    maze.append(list())
while i<r+1:
    mazeSlots=input()
    rowLen=len(mazeSlots)
    k=0; row=i-1
    while k<len(mazeSlots):
        maze[row].append(mazeSlots[k])
        k+=1
    i+=1
"""
for k in range(0,len(maze)):
    output=""
    for j in range(0,len(maze[k])):
        output+=maze[k][j]
    print(output)
"""
row=0; col=0
for k in range(0,len(maze)):
    for j in range(0,len(maze[k])):
        if maze[k][j]=="k":
            row=k; col=j
            origX=row; origY=col
moves=0; tries=0
while True:
    #is Kate staying on the exit
    if  row==r-1:
        gotOut=True
        break
    #is there way to the left
    if not col-1<0:
        if maze[row][col-1]==" ":
            noMoves=False; tries=0
            maze[row][col-1]="k"
            maze[row][col]="*"
            col -= 1
            moves+=1
            continue
        else:
            noMoves=True
    else:
        noMoves=True
    #is there way to the right
    if not col+1>=rowLen:
        if maze[row][col+1]==" ":
                noMoves = False; tries=0
                maze[row][col+1]="k"
                maze[row][col]="*"
                col += 1
                moves+=1
                continue
        else:
            noMoves=True
    else:
        noMoves=True
    #is there way up
    if not row-1<0:
        if maze[row-1][col]==" ":
            noMoves = False; tries=0
            maze[row-1][col]="k"
            maze[row][col]="*"
            row -= 1
            moves+=1
            continue
        else:
            noMoves=True
    else:
        noMoves=True
    #is there way down
    if not row+1>r-1:
        if maze[row+1][col]==" ":
            noMoves = False; tries=0
            maze[row+1][col]=="k"
            maze[row][col]="*"
            row += 1
            moves+=1
            if row==r-1:
                gotOut=True
                break
            continue
        else:
            noMoves=True
    else:
        gotOut=True
        noMoves=False
        break
    if noMoves==True:
        #get back and look for new ways
        if not col - 1 < 0:
            if maze[row][col-1]=="*":
                maze[row][col-1]=="k"
                maze[row][col]="-"
                col-=1
                moves-=1
        if not col + 1 >= rowLen:
            if maze[row][col+1]=="*":
                maze[row][col+1]="k"
                maze[row][col]="-"
                col+=1
                moves -= 1
        if not row - 1 < 0:
            if maze[row-1][col]=="*":
                maze[row-1][col]="k"
                maze[row][col]="-"
                row-=1
                moves -= 1
        if not row + 1 > r - 1:
            if maze[row+1][col]=="*":
                maze[row+1][col]="k"
                maze[row][col]="-"
                row+=1
                moves -= 1
        if row==origX and col==origY:
            tries+=1
            if tries==2:
                break
        noMoves=False
if gotOut==True:
    moves+=1
    print(f"Kate got out in {moves} moves")
else:
    print("Kate cannot get out")
#Not finished!
