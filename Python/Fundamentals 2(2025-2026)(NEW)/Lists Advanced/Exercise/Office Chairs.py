from functools import reduce

rooms = int(input())

rooms = [0 for k in range(0, rooms)]


for k in range(0, len(rooms)):
    info = input().split(" ")

    info[1] = int(info[1])
    info[0] = info[0].count("X")

    if info[0] >= info[1]:
        rooms[k] = info[0] - info[1]

    else:
        rooms[k] = info[0] - info[1]
        print(f"{abs(rooms[k])} more chairs needed in room {k + 1}")

totalFreeChairs = reduce(lambda a, x: a + x, rooms)

if totalFreeChairs > 0:
    print(f"Game On, {totalFreeChairs} free chairs left")