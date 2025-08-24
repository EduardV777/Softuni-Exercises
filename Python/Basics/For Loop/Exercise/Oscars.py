actorName = input()
academyPoints = float(input())
juryCount = int(input())
quali = False

for i in range(0, juryCount):
    juryName = input()
    juryPoints = float(input())

    academyPoints += (len(juryName) * juryPoints) / 2

    if academyPoints > 1250.5:
        quali = True
        break

if quali:
    print(f"Congratulations, {actorName} got a nominee for leading role with {academyPoints:.1f}!")
else:
    print(f"Sorry, {actorName} you need {abs(academyPoints - 1250.5):.1f} more!")