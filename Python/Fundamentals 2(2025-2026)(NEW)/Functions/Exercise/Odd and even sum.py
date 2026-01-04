n = input()

oddSum = 0
evenSum = 0

def evenCalc(sequence: str):
    evenSum = 0

    digits = [int(k) for k in sequence if int(k) % 2 == 0]
    for k in digits:
        evenSum += k

    return evenSum

def oddCalc(sequence: str):
    oddSum = 0

    digits = [int(k) for k in sequence if int(k) % 2 != 0]
    for k in digits:
        oddSum += k

    return oddSum

oddSum = oddCalc(n)
evenSum = evenCalc(n)

print(f"Odd sum = {oddSum}, Even sum = {evenSum}")