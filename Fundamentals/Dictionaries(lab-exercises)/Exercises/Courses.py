courses={}
while True:
    command=input()
    if command!="end":
        studentData=command.split(" : ")
        courseFound=False
        for j in courses:
            if j==studentData[0]:
                courseFound=True
                courses[j][0]+=1; courses[j][1].append(studentData[1])
                break
        if courseFound==False:
            courses[studentData[0]]=[1,[studentData[1]]]
    else:
        sortByRegStudents=sorted(courses.items(),key=lambda x: x[1], reverse=True)
        sortedByRegStudents=dict(sortByRegStudents)
        output=""
        for j in sortedByRegStudents:
            output+=f"{j}: {courses[j][0]}\n"
            courses[j][1].sort()
            for k in range(0,len(courses[j][1])):
                output+=f"-- {courses[j][1][k]}\n"
        print(output)
        break
