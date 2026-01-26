from math import pow

electrons = int(input())

def fillShells(electrons: int):
    shells = []
    pos = 1

    while True:
        electrons -= 2 * (pow(pos,2))

        if electrons > 0:
            shells.append(int(2 * (pow(pos,2))))
        else:
            electrons += 2 * (pow(pos,2))
            shells.append(int(electrons))
            electrons = 0
            break

        pos += 1

    return shells

shellsFilled = fillShells(electrons)

print(shellsFilled)