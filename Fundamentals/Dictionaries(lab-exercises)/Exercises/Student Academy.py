studentsData={}
n=int(input())
for k in range(0,n):
    studentName=input(); studentGrade=float(input())
    studentFound=False
    for j in studentsData:
        if studentName==j:
            studentFound=True
            studentsData[j][0]+=studentGrade; studentsData[j][1]+=1
            break
    if studentFound==False:
        studentsData[studentName]=[studentGrade, 1]

for j in studentsData:
    studentsData[j]=studentsData[j][0]/studentsData[j][1]
    
orderByAvgGrade=sorted(studentsData.items(),key=lambda x: x[1], reverse=True)
orderedStudentsData=dict(orderByAvgGrade)
for j in orderedStudentsData:
    if orderedStudentsData[j]>=4.5:
        print(f"{j} -> {orderedStudentsData[j]:.2f}")
