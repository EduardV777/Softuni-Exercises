empHappiness = input().split(" ")
hapImprovementFactor = int(input())


empHappiness = list(map(int,empHappiness))

def calculateHappiness(seq: list, factor: int):
    total = 0

    for k in range(0,len(seq)):
        seq[k] = seq[k] * factor
        total += seq[k]

    avg = total / len(seq)
    totalHappy = list(filter(lambda x: x >= avg, seq))

    return len(seq), avg, len(totalHappy)

res = calculateHappiness(empHappiness, hapImprovementFactor)

if res[2] >= res[0] / 2:
    print(f"Score: {res[2]}/{res[0]}. Employees are happy!")
else:
    print(f"Score: {res[2]}/{res[0]}. Employees are not happy!")