wagons = int(input())

train = []

for k in range(1, wagons + 1):
    train.append(0)

while True:
    command = input()

    if command != "End":
        command = command.split(" ")

        if command[0] == "add":
            people = int(command[1])

            train[-1] += people

        elif command[0] == "insert":
            wag = int(command[1])
            people = int(command[2])

            train[wag] += people

        elif command[0] == "leave":
            wag = int(command[1])
            people = int(command[2])

            train[wag] -= people

    else:
        break

print(train)