boardSize=int(input())
board=[]
knightsToRemove=0

def PrintBoard(board):
    output=""
    for k in range(0,len(board)):
        for j in range(0,len(board[k])):
            output+=str(board[k][j])
        output+="\n"
    return output


for k in range(0,boardSize):
    row=input()
    board.append([e for e in row])

#print(board)
#print(boardScheme)
for k in range(0,boardSize):
    for j in range(0,boardSize):
        pieceTaken=False
        #identify Knight
        if board[k][j]=="K":
            #can the knight move up?
            if not k-2<0:
                if not j-1<0:
                    if board[k-2][j-1]=="K":
                        board[k-2][j-1]="0"
                        #board[k][j]="0"
                        knightsToRemove += 1
                        pieceTaken=True
                if not j+1>=boardSize and pieceTaken==False:
                    if board[k-2][j+1]=="K":
                        board[k-2][j+1]="0"
                        #board[k][j] = "0"
                        knightsToRemove += 1
                        pieceTaken=True

            #can the knight move down?
            if not k+2>=boardSize and pieceTaken==False:
                if not j-1<0:
                    if board[k+2][j-1]=="K":
                        board[k+2][j-1]="0"
                        #board[k][j] = "0"
                        knightsToRemove += 1
                        pieceTaken=True
                if not j+1>=boardSize and pieceTaken==False:
                    if board[k+2][j+1]=="K":
                        board[k+2][j+1]="0"
                        #board[k][j] = "0"
                        knightsToRemove += 1
                        pieceTaken=True
            #can the knight move left?
            if not j-2<0 and pieceTaken==False:
                if not k-1<0:
                    if board[k-1][j-2]=="K":
                        board[k-1][j-2]="0"
                        #board[k][j] = "0"
                        knightsToRemove += 1
                        pieceTaken=True
                if not k+1>=boardSize and pieceTaken==False:
                    if board[k+1][j-2]=="K":
                        board[k+1][j-2]="0"
                        #board[k][j] = "0"
                        knightsToRemove += 1
                        pieceTaken = True
            #can the knight move right?
            if not j+2>=boardSize and pieceTaken==False:
                if not k-1<0:
                    if board[k-1][j+2]=="K":
                        board[k-1][j+2]="0"
                        #board[k][j] = "0"
                        knightsToRemove += 1
                        pieceTaken=True
                if not k+1>=boardSize and pieceTaken==False:
                    if board[k+1][j+2]=="K":
                        board[k+1][j+2]="0"
                        #board[k][j] = "0"
                        knightsToRemove+=1
                        pieceTaken = True

print(knightsToRemove)
#print(PrintBoard(board))