#one project takes three hours

architectName = input()
projectsN = int(input())

timePerProject = 3
totalHours = projectsN * timePerProject

print(f"The architect {architectName} will need {totalHours} hours to complete {projectsN} project/s.")