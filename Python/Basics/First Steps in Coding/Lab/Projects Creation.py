architectName = input()
projectsCount = int(input())

# each projects takes 3 hours
timePerProject = 3

neededHours = projectsCount * timePerProject

print(f"The architect {architectName} will need {neededHours} hours to complete {projectsCount} project/s.")