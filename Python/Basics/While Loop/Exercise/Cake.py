w = int(input())
l = int(input())

totalPieces = w * l

while totalPieces > 0:

    pieces = input()

    if pieces != "STOP":
        pieces = int(pieces)
        totalPieces -= pieces
    else:
        break

if totalPieces <= 0:
    print(f"No more cake left! You need {abs(totalPieces)} pieces more.")
else:
    print(f"{totalPieces} pieces are left.")