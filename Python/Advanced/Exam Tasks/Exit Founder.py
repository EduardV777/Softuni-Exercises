from collections import deque

def ShowMatrix(matrix):

    for k in range(0,6):
        output = ""
        for j in range(0,6):
            output += matrix[k][j]+" "

    print(output + "\n")



names = input().split(", ")
maze = ""
turns = deque(names)


for rows in range(0,6):
    row = input()
    maze += row

    if rows != 5:
        maze += "\n"

maze = maze.split("\n")
mazeBoard = []
restingPlayers = []

for k in range(0,len(maze)):
    mazeBoard.append([])
    maze[k] = maze[k].split(" ")

    for j in range(0,len(maze[k])):
        mazeBoard[k].append(maze[k][j])


def isNextPlayerResting(playerName):
    if("rest" in playerName):
        playerName = playerName.split(" ")[0]
    
    return playerName
            
            
            

while True:

    currPlayer = turns.popleft()
    coordinates = input().split(", ")
    coordinates[0] = int(coordinates[0].split("(")[1])
    coordinates[1] = int(coordinates[1].split(")")[0])


    if("rest" in currPlayer):
        #isNextPlayerResting()
        currPlayer = currPlayer.split(" ")[0]
        turns.append(currPlayer)
        continue

    turns.append(currPlayer)
    
    if(coordinates[0] > 5 or coordinates[1] > 5):
        pass
    else:


        if(mazeBoard[coordinates[0]][coordinates[1]] == "T"):
            nextPlayer = turns.popleft()
            print(f"{currPlayer} is out of the game! The winner is {isNextPlayerResting(nextPlayer)}.")
            break
        elif (mazeBoard[coordinates[0]][coordinates[1]] == "E"):
            print(f"{currPlayer} found the Exit and wins the game!")
            break
        elif (mazeBoard[coordinates[0]][coordinates[1]] == "W"):
            print(f"{currPlayer} hits a wall and needs to rest.")
            currPlayer += " rest"
            nextPlayer = turns.popleft()
            turns.popleft()
            turns.append(nextPlayer)
            turns.append(currPlayer)
        elif (mazeBoard[coordinates[0]][coordinates[1]] == "."):
            pass


"""

Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)
"""


"""

    • Only one Exit - marked with the "E" letter
    • Trap (one, many, or none) - marked with the "T" letter
    • Wall (one, many, or none) - marked with the "W" letter
    • Empty positions will be marked with "."

"""