matrix = []

n = 6
while n > 0:
    row = input().split(' ')
    matrix.append(row)
    n -= 1

firstPos = input()
x = int(firstPos[1])
y = int(firstPos[4])


while True:
    command = input()
    if command != "Stop":
        command = command.split(", ")
        
        if "Create" in command:
            val = command[2]
            direction = command[1]
            
            if direction == "up":
                if not x - 1 < 0:
                    x -= 1
                    if matrix[x][y] == ".":
                        matrix[x][y] = val
            elif direction == "down":
                if not x + 1 >= len(matrix):
                    x += 1
                    if matrix[x][y] == ".":
                        matrix[x][y] = val
            elif direction == "left":
                if not y - 1 < 0:
                    y -= 1
                    if matrix[x][y] == ".":
                        matrix[x][y] = val
            elif direction == "right":
                if not y + 1 >= len(matrix[x]):
                    y += 1
                    if matrix[x][y] == ".":
                        matrix[x][y] = val

        elif "Update" in command:
            val = command[2]
            direction = command[1]

            if direction == "up":
                if not x - 1 < 0:
                    x -= 1
                    if matrix[x][y] != ".":
                        matrix[x][y] = val
            elif direction == "down":
                if not x + 1 >= len(matrix):
                    x += 1
                    if matrix[x][y] != ".":
                        matrix[x][y] = val
            elif direction == "left":
                if not y - 1 < 0:
                    y -= 1
                    if matrix[x][y] != ".":
                        matrix[x][y] = val
            elif direction == "right":
                if not y + 1 >= len(matrix[x]):
                    y += 1
                    if matrix[x][y] != ".":
                        matrix[x][y] = val

        elif "Read" in command:
            direction = command[1]
            if direction == "up":
                if not x - 1 < 0:
                    x -= 1
                    if matrix[x][y] != ".":
                        print(matrix[x][y])
            elif direction == "down":
                if not x + 1 >= len(matrix):
                    x += 1
                    if matrix[x][y] != ".":
                        print(matrix[x][y])
            elif direction == "left":
                if not y - 1 < 0:
                    y -= 1
                    if matrix[x][y] != ".":
                        print(matrix[x][y])
            elif direction == "right":
                if not y + 1 >= len(matrix[x]):
                    y += 1
                    if matrix[x][y] != ".":
                        print(matrix[x][y])

        elif "Delete" in command:
            val = "."
            direction = command[1]

            if direction == "up":
                if not x - 1 < 0:
                    x -= 1
                    if matrix[x][y] != ".":
                        matrix[x][y] = val
            elif direction == "down":
                if not x + 1 >= len(matrix):
                    x += 1
                    if matrix[x][y] != ".":
                        matrix[x][y] = val
            elif direction == "left":
                if not y - 1 < 0:
                    y -= 1
                    if matrix[x][y] != ".":
                        matrix[x][y] = val
            elif direction == "right":
                if not y + 1 >= len(matrix[x]):
                    y += 1
                    if matrix[x][y] != ".":
                        matrix[x][y] = val
    else:
        output = ""
        for k in range(0, len(matrix)):
            for j in range(0, len(matrix[k])):
                output += matrix[k][j]
                if j != len(matrix[k]) - 1:
                    output += " "
            if k != len(matrix) - 1:
                output += "\n"

        print(output)
        break



"""
. . . . . .
. 6 . . . .
G . S . t S
. . 10 . . .
. 95 . . 8 .
. . P . . .
(1, 1)
Create, down, r
Update, right, e
Create, right, a
Read, right
Delete, right
Stop
"""


"""
. . . . . .  
. 6 . . . .  
. T . D . O  
. . 10 A . .  
. 95 . 80 5 .  
. . P . t .   
(2, 3)
Create, down, o
Delete, right
Read, up
Create, left, 20
Update, up, P
Stop
"""

"""
H 8 . . . .
70 i . . . .
t . . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .
(0, 0)
Read, right
Read, down
Read, left
Delete, down
Create, right, 10
Read, left
Stop
"""