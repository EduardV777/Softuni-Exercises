from collections import deque

waterAmount=int(input())
line=deque([])

while True:
    person=input()
    if person!="Start":
        line.append(person)
    else:
        break

while True:
    command=input()
    if command!="End":
        if 'refill' in command:
            command=command.split(" ")
            liters=int(command[1])
            waterAmount+=liters
        else:
            liters=int(command)
            if liters<=waterAmount:
                print(f"{line.popleft()} got water")
                waterAmount-=liters
            else:
                print(f"{line.popleft()} must wait")
    else:
        print(f"{waterAmount} liters left")
        break