maxBadGrades = int(input())
limit = 0
solvedProblems = 0
lastProblem = ""
avgScore = 0

while limit < maxBadGrades:

    problemName = input()

    if problemName == "Enough":
        break
    else:
        grade = int(input())
        if grade <= 4:
            limit += 1

        solvedProblems += 1

        avgScore += grade

    lastProblem = problemName

if limit == maxBadGrades:
    print(f"You need a break, {limit} poor grades.")
else:
    print(f"Average score: {avgScore / solvedProblems:.2f}")
    print(f"Number of problems: {solvedProblems}")
    print(f"Last problem: {lastProblem}")
