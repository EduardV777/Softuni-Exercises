n=int(input())
students={}
for k in range(0,n):
    name = input()
    grade=float(input())
    if not name in students:
        students[name]=[grade]
    else:
        students[name].append(grade)

for j in students:
    gradesCount=len(students[j]); gradesSum=0
    for k in range(0,len(students[j])):
        gradesSum+=students[j][k]
    students[j]=gradesSum/gradesCount
    if students[j]<4.50:
        students[j]="Doesn't pass"

for j in students:
    if students[j]=="Doesn't pass":
        continue
    else:
        print(f"{j} -> {students[j]:.2f}")
