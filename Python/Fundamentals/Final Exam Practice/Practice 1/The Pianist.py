pianoPieces={}
n=int(input())
for k in range(0,n):
    piece=input(); piece=piece.split("|")
    pieceName=piece[0]; composer=piece[1]; key=piece[2]
    pianoPieces[pieceName]=[composer,key]
while True:
    command=input()
    if command!="Stop":
        if "Add" in command:
            command=command.split("|")
            pieceName=command[1]; composer=command[2]; key=command[3]
            ifAdded=f"{pieceName} by {composer} in {key} added to the collection!"
            if pieceName in pianoPieces:
                print(f"{pieceName} is already in the collection!")
            else:
                pianoPieces[pieceName]=[composer,key]
                print(ifAdded)
        elif "Remove" in command:
            command = command.split("|")
            pieceName=command[1]
            if pieceName in pianoPieces:
                del pianoPieces[pieceName]
                print(f"Successfully removed {pieceName}!")
            else:
                print(f"Invalid operation! {pieceName} does not exist in the collection.")
        elif "ChangeKey" in command:
            command = command.split("|")
            pieceName=command[1]; newKey=command[2]
            if pieceName in pianoPieces:
                pianoPieces[pieceName][1]=newKey
                print(f"Changed the key of {pieceName} to {newKey}!")
            else:
                print(f"Invalid operation! {pieceName} does not exist in the collection.")
    else:
        for pieceName in pianoPieces:
            print(f"{pieceName} -> Composer: {pianoPieces[pieceName][0]}, Key: {pianoPieces[pieceName][1]}")
        break
