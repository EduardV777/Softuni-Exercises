studentName = input()
gradeClass = 1
totalGrade = 0.00
fail = 0

while gradeClass <= 12:
    grade = float(input())

    if grade >= 4.00:
        gradeClass += 1
        totalGrade += grade
    else:
        fail += 1

        if fail > 1:
            print(f"{studentName} has been excluded at {gradeClass} grade")
            break

    if gradeClass == 13:
        print(f"{studentName} graduated. Average grade: {totalGrade / 12:.2f}")
        break