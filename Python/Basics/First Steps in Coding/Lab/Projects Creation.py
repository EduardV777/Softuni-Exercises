architectName = input()
projectsN = int(input())
timePerProject = 3
#One project takes three hours to be created
hoursNeeded = projectsN * timePerProject
print(f"The architect {architectName} will need {hoursNeeded} hours to complete {projectsN} project/s.")