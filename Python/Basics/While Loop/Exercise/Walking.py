totalSteps = 0
goalSteps = 10000
going = True

while True:
    dailySteps = input()

    if dailySteps != "Going home":
        dailySteps = int(dailySteps)
        totalSteps += dailySteps

    else:
        stepsToHome = int(input())
        totalSteps += stepsToHome
        going = False

    if totalSteps >= goalSteps:
        print(f"Goal reached! Good job!\n{totalSteps - goalSteps} steps over the goal!")
        break
    else:
        if not going:
            print(f"{goalSteps - totalSteps} more steps to reach goal.")
            break
