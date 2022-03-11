courses={}

while True:
    command=input()
    if command!="end":
        command=command.split(" : ")
        doesCourseExist=False
        for j in courses:
            if j==command[0]:
                doesCourseExist=True
                break
        if doesCourseExist==False:
            courses[command[0]]=[command[1]]
        else:
            courses[command[0]].append(command[1])
    else:
        for j in courses:
            print(f"{j}: {len(courses[j])}")
            for k in range(0,len(courses[j])):
                print(f"-- {courses[j][k]}")
        break
