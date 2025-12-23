totalAvgScore = 0
presentations = 0
jurySize = int(input())

while True:
    presentationName = input()

    if presentationName != "Finish":
        presentations += 1
        score = 0
        for k in range(0, jurySize):
            grade = float(input())
            score += grade
            totalAvgScore += grade

        print(f"{presentationName} - {score / jurySize:.2f}.")

    else:
        break

print(f"Student's final assessment is {totalAvgScore / (jurySize * presentations):.2f}.")