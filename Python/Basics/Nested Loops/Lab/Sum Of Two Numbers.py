a = int(input())
b = int(input())
magicN = int(input())
n1 = a
n2 = a
combinationN = 0
found = False

while n1 <= b:
    while n2 <= b:
        combinationN += 1
        if n1 + n2 == magicN:
            print(f"Combination N:{combinationN} ({n1} + {n2} = {magicN})")
            found = True
            break
        n2 += 1

    if found:
        break
    else:
        n2 = a
        n1 += 1

if not found:
    print(f"{combinationN} combinations - neither equals {magicN}")