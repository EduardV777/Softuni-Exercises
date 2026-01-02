a=int(input()); b=int(input()); c=int(input())
studentsCount=int(input())
timeNeeded=0
while studentsCount>0:
    timeNeeded+=1
    if timeNeeded % 4 != 0:
        studentsCount -= a; studentsCount -= b; studentsCount -= c
print(f"Time needed: {timeNeeded}h.")

#SoftUni Reception
